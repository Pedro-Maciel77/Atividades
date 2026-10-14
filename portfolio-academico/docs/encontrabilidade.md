---
id: doc-encontrabilidade
titulo: "Encontrabilidade: nomes, palavras-chave e busca"
descricao: "Padrão de nomes de arquivos e pastas, descrição e topics do GitHub, palavras-chave, glossário e índice de busca."
tipo: documentacao
fase_pi: nenhuma
ucs: []
escopo: individual
autores: [pedro-henrique-maciel]
data: 2026-10-13
status: em-andamento
tags: [arquitetura-da-informacao, github]
relacionados: [doc-arquitetura-da-informacao, doc-metadados, doc-passo-a-passo-git]
---

# Encontrabilidade: nomes, palavras-chave e busca

Encontrabilidade é a facilidade de achar um conteúdo. Neste repositório isso acontece de três jeitos: **navegando**, **buscando** e **filtrando por tag**.

## Padrão de nomes

| Item | Regra | Exemplo |
|------|-------|---------|
| Pastas | minúsculas, sem acento, sem espaço, com hífen | `empreendedorismo` |
| Fases do PI | `NN-nome` | `03-modelagem-de-negocio` |
| Documentos | `NN-slug.md` (número + nome curto) | `09-lean-canvas.md` |
| Anexos | mesmo nome do documento, outra extensão | `09-lean-canvas.pdf` |
| Índices | sempre `README.md` | `ucs/gestao-da-informacao/README.md` |
| ids | prefixo + número + slug | `pi-09-lean-canvas` |

**Slug:** nome curto em português, em minúsculas, sem acento e com hífens. "Mapa de Empatia" vira `mapa-de-empatia`.

**Evite:** espaços, acentos, maiúsculas e nomes como `final`, `final2`, `novo`.

## Repositório no GitHub

**Nome:** `portfolio-academico`

**Descrição (campo "About"):**

> Portfólio acadêmico de Pedro Henrique Maciel (ADS, Senac): atividades das UCs e do Projeto Integrador Altura, organizadas com Arquitetura da Informação.

**Topics:**

```
portfolio, portfolio-academico, senac, projeto-integrador,
analise-e-desenvolvimento-de-sistemas, arquitetura-da-informacao,
startups, investidores, matchmaking, react, typescript
```

Os comandos para configurar isso estão em [passo a passo do git](passo-a-passo-git.md).

## Palavras-chave

portfólio acadêmico · Projeto Integrador · PI · Altura · NEXO · Senac · Análise e Desenvolvimento de Sistemas · Gestão da Informação · Empreendedorismo · Plano de Negócios · startups · investidores · matchmaking · compatibilidade · persona · mapa de empatia · Customer Discovery · Jobs to Be Done · Business Model Canvas · Lean Canvas · MVP · PWA · React · TypeScript · Vite · Node.js · LGPD · Arquitetura da Informação

## Como achar algo

| Quero... | Vá em... |
|----------|----------|
| Ver tudo o que existe | [SUMARIO.md](../SUMARIO.md) |
| Buscar por assunto, tipo, fase ou status | [INDEX.md](../INDEX.md) |
| Ver os dados de todos os documentos | [catalogo.yml](../catalogo.yml) |
| Entender um termo | [GLOSSARIO.md](../GLOSSARIO.md) |
| Achar um arquivo pelo nome | tecla `t` na página do repositório no GitHub |
| Achar um texto | campo de busca do GitHub, ou `Ctrl+F` no INDEX.md |

## Índice de busca e catálogo

`INDEX.md` e `catalogo.yml` são gerados pelo script `scripts/atualizar.py` a partir dos [metadados](metadados.md). O índice lista os documentos:

- todos juntos, em uma tabela;
- por fase do PI, por UC, por tipo e por status;
- por tag (cada tag leva aos documentos que a usam);
- por relação (quem se liga a quem).

---

[← Anterior: Metadados](metadados.md) | [↑ README](../README.md) | [Próximo: Relações →](relacoes.md)
