---
id: doc-metadados
titulo: "Metadados: padrão de cabeçalho (front matter)"
descricao: "Define os campos do cabeçalho YAML de cada documento e mostra um exemplo preenchido com o Mapa de Empatia do Altura."
tipo: documentacao
fase_pi: nenhuma
ucs: []
escopo: individual
autores: [pedro-henrique-maciel]
data: 2026-10-13
status: em-andamento
tags: [arquitetura-da-informacao]
relacionados: [doc-arquitetura-da-informacao, doc-taxonomia, doc-encontrabilidade]
---

# Metadados: padrão de cabeçalho (front matter)

Todo documento começa com um bloco entre `---` escrito em YAML. Ele descreve o documento e é lido pelo script `scripts/atualizar.py` para gerar o [INDEX.md](../INDEX.md) e o [catalogo.yml](../catalogo.yml).

## Campos

| Campo | Obrigatório | O que colocar |
|-------|-------------|---------------|
| `id` | sim | Identificador único: prefixo + número + slug. Ex.: `pi-02-mapa-de-empatia` |
| `titulo` | sim | Título legível. Use aspas se tiver `:` |
| `descricao` | sim | Uma frase dizendo o que é o documento |
| `tipo` | sim | Um termo de [tipo](taxonomia.md#tipo-de-documento) |
| `fase_pi` | sim | Um termo de [fase do PI](taxonomia.md#fase-do-pi), ou `nenhuma` |
| `ucs` | sim | Lista de [UCs](taxonomia.md#uc-unidade-curricular). Pode ser `[]` |
| `escopo` | sim | `grupo` ou `individual` |
| `autores` | sim | Lista. Use `equipe-altura` para trabalho do grupo e `pedro-henrique-maciel` para o meu |
| `data` | sim | `AAAA-MM-DD` |
| `status` | sim | Um termo de [status](taxonomia.md#status) |
| `tags` | sim | Lista de [tags](taxonomia.md#tags-de-tecnologia) da taxonomia. Pode ser `[]` |
| `relacionados` | sim | Lista de `id` de outros documentos. Pode ser `[]` |
| `arquivo_original` | não | Link ou nome do arquivo original (PDF, Google Forms, repositório) |

## Prefixos de id

| Prefixo | Uso |
|---------|-----|
| `pi-` | Documentos do Projeto Integrador |
| `doc-` | Documentos que explicam o repositório |
| `fs-` | Atividades da UC Gestão da Informação |
| `emp-` | Atividades da UC Empreendedorismo |
| [PREENCHER] | Prefixo para cada outra UC |

## Regras

- Use só termos que existem em [taxonomia.yml](../taxonomia.yml).
- Quando não souber um valor, escreva `"[PREENCHER]"` (com aspas) e complete depois.
- Se A lista B em `relacionados`, B deve listar A também. O script avisa quando isso não acontece.
- `data` é a data do documento (ou da última versão importante).

## Exemplo preenchido: Mapa de Empatia do Altura

Arquivo: [02-mapa-de-empatia.md](../pi-altura/01-pesquisa-e-empatia/02-mapa-de-empatia.md)

```yaml
---
id: pi-02-mapa-de-empatia
titulo: "Mapa de Empatia (público: startups)"
descricao: "Mapa de empatia do público startups, datado de 16/09/2026, feito pelo grupo do PI."
tipo: mapa-de-empatia
fase_pi: pesquisa-empatia
ucs: []
escopo: grupo
autores: [equipe-altura]
data: 2026-09-16
status: "[PREENCHER]"
tags: [empatia, startups]
relacionados: [pi-01-pesquisa-inicial, pi-03-plano-de-pesquisa, pi-04-persona-marina-duarte]
arquivo_original: "[PREENCHER]"
---
```

## Modelo em branco

Copie [templates/documento.md](../templates/documento.md) e troque os valores.

---

[← Anterior: Taxonomia](taxonomia.md) | [↑ README](../README.md) | [Próximo: Encontrabilidade →](encontrabilidade.md)
