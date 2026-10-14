#!/usr/bin/env python3
"""Atualiza e valida o repositório.

Uso (na raiz do repositório):
    python scripts/atualizar.py

O que faz:
1. Lê o front matter (YAML) de todos os .md que têm o campo "id".
2. Valida campos, termos da taxonomia, documentos relacionados e links relativos.
3. Gera INDEX.md, catalogo.yml e docs/taxonomia.md.

Requer: pip install pyyaml
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
PASTAS_IGNORADAS = {".git", "templates", "scripts", "node_modules"}
PLACEHOLDER = "[PREENCHER"
OBRIGATORIOS = [
    "id", "titulo", "descricao", "tipo", "fase_pi", "ucs", "escopo",
    "autores", "data", "status", "tags", "relacionados",
]


# ---------- leitura ----------

def arquivos_md():
    for p in sorted(RAIZ.rglob("*.md")):
        partes = p.relative_to(RAIZ).parts
        if not any(parte in PASTAS_IGNORADAS for parte in partes):
            yield p


def ler_front_matter(caminho):
    texto = caminho.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return None
    dados = yaml.safe_load(m.group(1))
    return dados if isinstance(dados, dict) else None


def carregar_documentos():
    docs = []
    for p in arquivos_md():
        fm = ler_front_matter(p)
        if fm and "id" in fm:
            fm["_caminho"] = p.relative_to(RAIZ).as_posix()
            docs.append(fm)
    return docs


def carregar_taxonomia():
    return yaml.safe_load((RAIZ / "taxonomia.yml").read_text(encoding="utf-8"))


# ---------- validação ----------

def sem_codigo(texto):
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", texto)


def slug(titulo):
    titulo = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", titulo)
    titulo = re.sub(r"[`*]", "", titulo).strip().lower()
    titulo = re.sub(r"[^\w\- ]", "", titulo)
    return titulo.replace(" ", "-")


def ancoras(caminho):
    texto = re.sub(r"```.*?```", "", caminho.read_text(encoding="utf-8"), flags=re.S)
    return {slug(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.*)$", texto, re.M)}


def validar(docs, tax):
    erros, avisos = [], []
    tags_validas = {t for grupo in tax["tags"].values() for t in grupo}
    ids = {}
    for d in docs:
        onde = d["_caminho"]
        for campo in OBRIGATORIOS:
            if campo not in d:
                erros.append(f"{onde}: falta o campo '{campo}'")
        if d["id"] in ids:
            erros.append(f"{onde}: id repetido ({d['id']}) também em {ids[d['id']]}")
        ids[d["id"]] = onde

        def checar(campo, valor, validos):
            if str(valor).startswith(PLACEHOLDER):
                return
            if valor not in validos:
                erros.append(f"{onde}: {campo} '{valor}' não está na taxonomia")

        checar("tipo", d.get("tipo"), tax["tipo"])
        checar("fase_pi", d.get("fase_pi"), tax["fase_pi"])
        checar("escopo", d.get("escopo"), tax["escopo"])
        checar("status", d.get("status"), tax["status"])
        for uc in d.get("ucs") or []:
            checar("uc", uc, tax["ucs"])
        for tag in d.get("tags") or []:
            checar("tag", tag, tags_validas)

    por_id = {d["id"]: d for d in docs}
    for d in docs:
        for rel in d.get("relacionados") or []:
            if rel not in por_id:
                erros.append(f"{d['_caminho']}: relacionado '{rel}' não existe")
            elif d["id"] not in (por_id[rel].get("relacionados") or []):
                avisos.append(f"{d['_caminho']} aponta para {rel}, mas {rel} não aponta de volta")

    for p in arquivos_md():
        texto = sem_codigo(p.read_text(encoding="utf-8"))
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", texto):
            alvo = m.group(1)
            if alvo.startswith(("http://", "https://", "mailto:")):
                continue
            arquivo, _, ancora = alvo.partition("#")
            destino = (p.parent / arquivo).resolve() if arquivo else p
            nome = p.relative_to(RAIZ).as_posix()
            if not destino.exists():
                erros.append(f"{nome}: link quebrado -> {alvo}")
            elif ancora and destino.suffix == ".md" and ancora not in ancoras(destino):
                erros.append(f"{nome}: âncora inexistente -> {alvo}")
    return erros, avisos


def contar_pendencias():
    contagem = {}
    for p in arquivos_md():
        if p.name == "INDEX.md":  # gerado: repete os marcadores dos documentos
            continue
        n = sem_codigo(p.read_text(encoding="utf-8")).count(PLACEHOLDER)
        if n:
            contagem[p.relative_to(RAIZ).as_posix()] = n
    return contagem


# ---------- geração ----------

def link(d, base=""):
    return f"[{d['titulo']}]({base}{d['_caminho']})"


def gerar_catalogo(docs):
    saida = []
    for d in docs:
        item = {k: v for k, v in d.items() if not k.startswith("_")}
        item["caminho"] = d["_caminho"]
        if "data" in item:
            item["data"] = str(item["data"])
        saida.append(item)
    cabecalho = (
        "# Catálogo de documentos (gerado por scripts/atualizar.py). Não edite à mão.\n"
        "# Para mudar algo, edite o front matter do documento e rode o script de novo.\n"
    )
    corpo = yaml.safe_dump(saida, allow_unicode=True, sort_keys=False, width=100)
    (RAIZ / "catalogo.yml").write_text(cabecalho + corpo, encoding="utf-8")


def gerar_indice(docs, tax):
    L = []
    L.append("# Índice de busca\n")
    L.append(
        "Lista de todos os documentos do repositório, organizada de várias formas. "
        "Use o `Ctrl+F` do navegador ou a busca do GitHub para achar um termo. "
        "Os mesmos dados estão em [catalogo.yml](catalogo.yml).\n"
    )
    L.append("> Arquivo gerado por `python scripts/atualizar.py`. Não edite à mão.\n")

    L.append("## Todos os documentos\n")
    L.append("| Documento | Tipo | Fase do PI | UC | Escopo | Status | Data |")
    L.append("|-----------|------|------------|----|--------|--------|------|")
    for d in docs:
        ucs = ", ".join(d.get("ucs") or []) or "-"
        L.append(
            f"| {link(d)} | {d['tipo']} | {d['fase_pi']} | {ucs} | {d['escopo']} | "
            f"{d['status']} | {d['data']} |"
        )
    L.append("")

    def agrupar(titulo, chave, termos, lista=False):
        L.append(f"## {titulo}\n")
        grupos = defaultdict(list)
        for d in docs:
            valores = (d.get(chave) or []) if lista else [d.get(chave)]
            for v in valores:
                grupos[v].append(d)
        for termo in termos:
            if grupos.get(termo):
                L.append(f"**{termo}**\n")
                for d in grupos[termo]:
                    L.append(f"- {link(d)}")
                L.append("")

    agrupar("Por fase do PI", "fase_pi", tax["fase_pi"])
    agrupar("Por UC", "ucs", tax["ucs"], lista=True)
    agrupar("Por tipo", "tipo", tax["tipo"])
    agrupar("Por status", "status", tax["status"])

    L.append("## Por tag\n")
    por_tag = defaultdict(list)
    for d in docs:
        for t in d.get("tags") or []:
            por_tag[t].append(d)
    for tag in sorted(por_tag):
        itens = "; ".join(link(d) for d in por_tag[tag])
        L.append(f"- **{tag}**: {itens}")
    L.append("")

    L.append("## Relações entre documentos\n")
    L.append("| Documento | Relacionado com |")
    L.append("|-----------|-----------------|")
    por_id = {d["id"]: d for d in docs}
    for d in docs:
        rels = [link(por_id[r]) for r in d.get("relacionados") or [] if r in por_id]
        if rels:
            L.append(f"| {link(d)} | {'; '.join(rels)} |")
    L.append("")
    L.append("---\n")
    L.append("[← Voltar ao README](README.md) | [Sumário geral](SUMARIO.md) | [Glossário](GLOSSARIO.md)")
    (RAIZ / "INDEX.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def gerar_taxonomia_md(tax):
    L = [
        "---",
        "id: doc-taxonomia",
        'titulo: "Taxonomia: vocabulário controlado"',
        'descricao: "Lista de todos os termos permitidos em UC, fase do PI, tipo, escopo, status e tags, com definição."',
        "tipo: documentacao",
        "fase_pi: nenhuma",
        "ucs: []",
        "escopo: individual",
        "autores: [pedro-henrique-maciel]",
        "data: 2026-10-13",
        "status: em-andamento",
        "tags: [arquitetura-da-informacao]",
        "relacionados: [doc-arquitetura-da-informacao, doc-classificacao, doc-metadados]",
        "---",
        "",
        "# Taxonomia: vocabulário controlado",
        "",
        "> Arquivo gerado a partir de `taxonomia.yml` por `python scripts/atualizar.py`. "
        "Para criar ou mudar um termo, edite o `taxonomia.yml`, não este arquivo.",
        "",
        "Só os termos abaixo podem aparecer nos metadados dos documentos. "
        "Assim, a mesma coisa sempre tem o mesmo nome e a busca funciona.",
        "",
    ]

    def tabela(titulo, campo, termos):
        L.append(f"## {titulo}\n")
        L.append(f"Campo do front matter: `{campo}`\n")
        L.append("| Termo | Definição |")
        L.append("|-------|-----------|")
        for termo, definicao in termos.items():
            L.append(f"| `{termo}` | {definicao} |")
        L.append("")

    tabela("UC (Unidade Curricular)", "ucs", tax["ucs"])
    tabela("Fase do PI", "fase_pi", tax["fase_pi"])
    tabela("Tipo de documento", "tipo", tax["tipo"])
    tabela("Escopo", "escopo", tax["escopo"])
    tabela("Status", "status", tax["status"])
    nomes = {"tecnologia": "Tags de tecnologia", "metodo": "Tags de método", "tema": "Tags de tema"}
    for grupo, termos in tax["tags"].items():
        tabela(nomes.get(grupo, f"Tags: {grupo}"), "tags", termos)
    L.append("---\n")
    L.append("[← Anterior: Classificação](classificacao.md) | [↑ README](../README.md) | [Próximo: Metadados →](metadados.md)")
    (RAIZ / "docs" / "taxonomia.md").write_text("\n".join(L) + "\n", encoding="utf-8")


# ---------- principal ----------

def main():
    tax = carregar_taxonomia()
    gerar_taxonomia_md(tax)  # antes de ler os docs, para o novo arquivo entrar no catálogo
    docs = carregar_documentos()
    gerar_catalogo(docs)  # gerar antes de validar, para os links para INDEX.md existirem
    gerar_indice(docs, tax)
    erros, avisos = validar(docs, tax)

    print(f"{len(docs)} documentos catalogados.")
    for a in avisos:
        print("AVISO:", a)
    for e in erros:
        print("ERRO: ", e)
    pend = contar_pendencias()
    total = sum(pend.values())
    print(f"\n{total} marcadores [PREENCHER] em {len(pend)} arquivos:")
    for arq, n in sorted(pend.items()):
        print(f"  {n:3d}  {arq}")
    if erros:
        print(f"\n{len(erros)} erro(s). Corrija e rode de novo.")
        sys.exit(1)
    print("\nTudo certo.")


if __name__ == "__main__":
    main()
