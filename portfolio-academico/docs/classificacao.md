---
id: doc-classificacao
titulo: "Classificação e estrutura de pastas"
descricao: "Mostra a árvore de pastas do repositório e justifica o critério de classificação escolhido."
tipo: documentacao
fase_pi: nenhuma
ucs: []
escopo: individual
autores: [pedro-henrique-maciel]
data: 2026-10-13
status: em-andamento
tags: [arquitetura-da-informacao]
relacionados: [doc-arquitetura-da-informacao, doc-taxonomia]
---

# Classificação e estrutura de pastas

## Estrutura

```
portfolio-academico/
├── README.md                     página inicial do portfólio
├── SUMARIO.md                    sumário geral
├── INDEX.md                      índice de busca (gerado)
├── GLOSSARIO.md                  termos do curso e do projeto
├── CONTRIBUINDO.md               como adicionar conteúdo novo
├── catalogo.yml                  catálogo dos documentos (gerado)
├── taxonomia.yml                 vocabulário controlado
├── docs/                         explicação da Arquitetura da Informação
├── ucs/                          atividades individuais, por UC
│   ├── README.md                 índice de UCs
│   ├── gestao-da-informacao/
│   └── empreendedorismo/
├── pi-altura/                    Projeto Integrador (trabalho do grupo)
│   ├── README.md                 índice do PI
│   ├── 01-pesquisa-e-empatia/    documentos 01 a 05
│   ├── 02-customer-discovery/    documentos 06 e 07
│   ├── 03-modelagem-de-negocio/  documentos 08 e 09
│   └── 04-mvp/                   documento 10
├── templates/                    modelos para novos documentos
└── scripts/                      script que gera índices e valida tudo
```

## Por que classifiquei assim

Misturei dois critérios porque o conteúdo é de dois tipos:

1. **Por UC** (`ucs/`). O semestre é dividido em UCs e o professor avalia por UC. Atividades individuais ficam aqui, uma pasta por UC.
2. **Por fase do PI** (`pi-altura/`). O PI é um só projeto que atravessa várias UCs, então não cabe dentro de uma UC. Dentro dele, as pastas seguem a história do projeto, do problema até a solução: pesquisa, discovery, modelagem e MVP. A numeração (01 a 10) mantém a ordem.

**O que não virou pasta:** o tipo de documento (canvas, persona, questionário) e as tecnologias. Esses critérios cortam todas as pastas, então ficam nos **metadados e tags** ([taxonomia](taxonomia.md)). Assim cada documento tem um único endereço e pode ser achado por vários caminhos.

## Regras de classificação

- Cada documento fica em um único lugar.
- No máximo dois níveis de pasta dentro de `ucs/` e de `pi-altura/`.
- Atividade de UC vai em `ucs/<uc>/`. Documento do PI vai em `pi-altura/<fase>/`.
- Se uma atividade de UC alimenta o PI, ela fica na UC e é ligada ao PI pelo campo `relacionados`.

---

[← Anterior: Arquitetura da Informação](arquitetura-da-informacao.md) | [↑ README](../README.md) | [Próximo: Taxonomia →](taxonomia.md)
