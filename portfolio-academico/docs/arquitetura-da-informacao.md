---
id: doc-arquitetura-da-informacao
titulo: "Arquitetura da Informação neste repositório"
descricao: "Explica como classificação, taxonomia, metadados, navegação, encontrabilidade e relações entre conteúdos foram aplicados."
tipo: documentacao
fase_pi: nenhuma
ucs: []
escopo: individual
autores: [pedro-henrique-maciel]
data: 2026-10-13
status: em-andamento
tags: [arquitetura-da-informacao, git, github]
relacionados: [doc-classificacao, doc-taxonomia, doc-metadados, doc-encontrabilidade, doc-relacoes]
---

# Arquitetura da Informação neste repositório

Este documento mostra como apliquei, neste repositório, os 6 conceitos de Arquitetura da Informação pedidos na atividade. Cada seção tem a ideia, o que eu fiz e onde ver.

**Autoria:** a atividade e este repositório são **individuais**. Os documentos do Projeto Integrador (PI) são **do grupo**; por isso cada um tem o campo `escopo: grupo`.

## Resumo

| Conceito | Como foi aplicado | Onde ver |
|----------|-------------------|----------|
| Classificação | Duas pastas principais (UCs e PI) e, dentro do PI, as 4 fases | [Classificação](classificacao.md) |
| Taxonomia | Vocabulário controlado com UC, fase, tipo, escopo, status e tags | [Taxonomia](taxonomia.md) |
| Metadados | Cabeçalho YAML padrão em todo documento | [Metadados](metadados.md) |
| Navegação | README, sumário, índices e links de anterior/próximo | seção abaixo |
| Encontrabilidade | Nomes padronizados, topics, glossário, índice e catálogo | [Encontrabilidade](encontrabilidade.md) |
| Relações entre conteúdos | Campo `relacionados`, seção "Relações" e mapa em Mermaid | [Relações](relacoes.md) |

## 1. Classificação

**Ideia:** agrupar conteúdos parecidos usando um critério.

**O que fiz:** usei dois critérios, um para cada tipo de conteúdo.

- `ucs/`: atividades individuais, agrupadas **por UC**, que é como o curso e o professor organizam o semestre.
- `pi-altura/`: documentos do PI, agrupados **por fase**, na ordem em que o grupo trabalhou (pesquisa, discovery, modelagem, MVP). Os arquivos são numerados de 01 a 10.

Cada documento mora em **um único lugar**. O tipo de documento (canvas, persona etc.) não vira pasta: vira metadado, para não duplicar arquivos.

**Onde ver:** [Classificação e estrutura de pastas](classificacao.md).

## 2. Taxonomia

**Ideia:** uma lista organizada de categorias e termos permitidos (vocabulário controlado).

**O que fiz:** o arquivo [taxonomia.yml](../taxonomia.yml) define todos os termos aceitos, com definição curta: UC, fase do PI, tipo de documento, escopo, status e tags (tecnologia, método e tema). O script `scripts/atualizar.py` recusa termos que não estão na lista, então o mesmo assunto nunca aparece com dois nomes.

**Onde ver:** [Taxonomia](taxonomia.md).

## 3. Metadados

**Ideia:** dados que descrevem o documento.

**O que fiz:** todo documento começa com um cabeçalho YAML (front matter) com `id`, `titulo`, `descricao`, `tipo`, `fase_pi`, `ucs`, `escopo`, `autores`, `data`, `status`, `tags` e `relacionados`. Há um modelo pronto em [templates/documento.md](../templates/documento.md) e um exemplo preenchido com o Mapa de Empatia do Altura.

**Onde ver:** [Metadados](metadados.md).

## 4. Navegação

**Ideia:** caminhos para a pessoa se mover entre os conteúdos sem se perder.

**O que fiz:**

- **Página inicial:** o [README](../README.md) apresenta o portfólio e leva a tudo.
- **Sumário geral:** o [SUMARIO](../SUMARIO.md) lista todas as páginas do repositório.
- **Índices:** um por UC ([ucs/README.md](../ucs/README.md) e o README de cada UC) e um do PI ([pi-altura/README.md](../pi-altura/README.md)), organizado por fase.
- **Anterior e próximo:** todo documento termina com `← Anterior | ↑ Índice | Próximo →`, seguindo a ordem numerada.
- **Voltar:** índices e READMEs sempre têm link para a página de cima.

**Exemplo:** o rodapé do [Mapa de Empatia](../pi-altura/01-pesquisa-e-empatia/02-mapa-de-empatia.md).

## 5. Encontrabilidade

**Ideia:** facilidade de achar um conteúdo, navegando ou buscando.

**O que fiz:**

- **Nomes padronizados:** `NN-slug-sem-acento.md`, pastas em minúsculas e com hífens.
- **GitHub:** descrição curta e topics no repositório.
- **Palavras-chave:** lista no README e em [Encontrabilidade](encontrabilidade.md).
- **Glossário:** [GLOSSARIO.md](../GLOSSARIO.md) explica os termos do curso e do projeto.
- **Índice de busca:** [INDEX.md](../INDEX.md) lista os documentos por fase, UC, tipo, status e tag.
- **Catálogo:** [catalogo.yml](../catalogo.yml), com os metadados de todos os documentos em um só lugar.

`INDEX.md` e `catalogo.yml` são gerados pelo script a partir dos metadados, então não ficam desatualizados.

**Onde ver:** [Encontrabilidade](encontrabilidade.md).

## 6. Relações entre conteúdos

**Ideia:** ligar documentos que se completam ou dependem uns dos outros.

**O que fiz:**

- Campo `relacionados` nos metadados (lista de ids).
- Seção "Relações" em cada documento, com links e o motivo da ligação.
- [Mapa de relações em Mermaid](relacoes.md), com a cadeia Persona → Mapa de Empatia → Plano de Pesquisa → Lean Canvas e as ligações com as UCs.
- Tabela de relações no [INDEX.md](../INDEX.md), gerada automaticamente.

**Onde ver:** [Relações entre conteúdos](relacoes.md).

## Como manter

Para adicionar uma atividade nova, basta seguir o [CONTRIBUINDO.md](../CONTRIBUINDO.md): copiar o modelo, preencher o cabeçalho com termos da taxonomia, ajustar anterior/próximo e rodar `python scripts/atualizar.py`.

---

[← Voltar ao README](../README.md) | [↑ Sumário](../SUMARIO.md) | [Próximo: Classificação →](classificacao.md)
