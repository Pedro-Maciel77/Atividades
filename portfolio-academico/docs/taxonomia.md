---
id: doc-taxonomia
titulo: "Taxonomia: vocabulário controlado"
descricao: "Lista de todos os termos permitidos em UC, fase do PI, tipo, escopo, status e tags, com definição."
tipo: documentacao
fase_pi: nenhuma
ucs: []
escopo: individual
autores: [pedro-henrique-maciel]
data: 2026-10-13
status: em-andamento
tags: [arquitetura-da-informacao]
relacionados: [doc-arquitetura-da-informacao, doc-classificacao, doc-metadados]
---

# Taxonomia: vocabulário controlado

> Arquivo gerado a partir de `taxonomia.yml` por `python scripts/atualizar.py`. Para criar ou mudar um termo, edite o `taxonomia.yml`, não este arquivo.

Só os termos abaixo podem aparecer nos metadados dos documentos. Assim, a mesma coisa sempre tem o mesmo nome e a busca funciona.

## UC (Unidade Curricular)

Campo do front matter: `ucs`

| Termo | Definição |
|-------|-----------|
| `fullstack` | UC FullStack. No PI, é a UC do desenvolvimento do MVP. |
| `empreendedorismo-plano-de-negocios` | UC de Empreendedorismo e Plano de Negócios. A aula 4 tratou de Customer Discovery e Jobs to Be Done. |

## Fase do PI

Campo do front matter: `fase_pi`

| Termo | Definição |
|-------|-----------|
| `pesquisa-empatia` | Fase 1. Pesquisa inicial com usuários e materiais para entender o público: mapa de empatia, plano de pesquisa e persona. |
| `customer-discovery` | Fase 2. Customer Discovery e Jobs to Be Done: instrumentos para conversar com o público e validar o problema. |
| `modelagem-negocio` | Fase 3. Modelagem do negócio com Business Model Canvas e Lean Canvas. |
| `mvp` | Fase 4. Desenvolvimento do MVP (UC FullStack). |
| `nenhuma` | Documento de uma UC que não faz parte do PI. |

## Tipo de documento

Campo do front matter: `tipo`

| Termo | Definição |
|-------|-----------|
| `pesquisa` | Relatório ou resumo de uma pesquisa. |
| `mapa-de-empatia` | Mapa que organiza o que o público pensa, sente, vê, ouve, fala e faz. |
| `plano` | Plano de trabalho, por exemplo o plano de pesquisa. |
| `persona` | Personagem que representa o usuário ideal do produto. |
| `tabela` | Tabela de dados ou de respostas, por exemplo a tabela de dimensões da equipe. |
| `canvas` | Quadro visual de modelo de negócio (Business Model Canvas ou Lean Canvas). |
| `questionario` | Roteiro de perguntas para entrevistas. |
| `formulario` | Formulário online para coletar respostas. |
| `codigo` | Código-fonte de um software. |
| `atividade` | Entrega ou exercício de uma UC. |
| `documentacao` | Documento que explica o próprio repositório. |

## Escopo

Campo do front matter: `escopo`

| Termo | Definição |
|-------|-----------|
| `grupo` | Trabalho feito em equipe (PI). |
| `individual` | Trabalho feito só por mim. |

## Status

Campo do front matter: `status`

| Termo | Definição |
|-------|-----------|
| `rascunho` | Em escrita. Não é a versão final. |
| `em-andamento` | Em produção, com parte já pronta. |
| `em-revisao` | Pronto, aguardando revisão ou feedback. |
| `concluido` | Versão final entregue. |

## Tags de tecnologia

Campo do front matter: `tags`

| Termo | Definição |
|-------|-----------|
| `react` | Biblioteca para criar interfaces (React 19 no MVP). |
| `typescript` | JavaScript com tipos. |
| `vite` | Ferramenta de desenvolvimento e build do front-end. |
| `nodejs` | JavaScript no servidor. Usado no back-end do MVP. |
| `pwa` | Progressive Web App: site que funciona como aplicativo instalável. |
| `banco-de-dados` | Armazenamento dos dados do sistema (em desenvolvimento no MVP). |
| `google-forms` | Ferramenta do Google para formulários online. |
| `git` | Sistema de controle de versão. |
| `github` | Plataforma que hospeda repositórios git. |

## Tags de método

Campo do front matter: `tags`

| Termo | Definição |
|-------|-----------|
| `pesquisa-com-usuarios` | Pesquisa para entender as necessidades de quem vai usar o produto. |
| `entrevista` | Conversa guiada por roteiro. |
| `empatia` | Técnicas para entender o que o usuário pensa, sente, faz e precisa. |
| `persona` | Uso de persona para representar o usuário. |
| `customer-discovery` | Conversar com potenciais clientes para validar o problema antes de construir. |
| `jtbd` | Jobs to Be Done: entender o trabalho que a pessoa quer resolver ao usar um produto. |
| `business-model-canvas` | Método de 9 blocos para desenhar um modelo de negócio. |
| `lean-canvas` | Variação do canvas focada em problema, solução e métricas. |

## Tags de tema

Campo do front matter: `tags`

| Termo | Definição |
|-------|-----------|
| `startups` | Empresas nascentes de base inovadora. |
| `investidores` | Pessoas e fundos que investem em startups. |
| `fundadores` | Pessoas que fundam startups. |
| `matchmaking` | Aproximar duas partes compatíveis, aqui startups e investidores. |
| `compatibilidade` | Percentual calculado pelo algoritmo do Altura entre startup e investidor. |
| `modelo-de-negocio` | Como o produto cria valor e gera receita. |
| `lgpd` | Lei Geral de Proteção de Dados Pessoais (conformidade planejada no Altura). |
| `arquitetura-da-informacao` | Organização e recuperação de informação, conceitos aplicados neste repositório. |

---

[← Anterior: Classificação](classificacao.md) | [↑ README](../README.md) | [Próximo: Metadados →](metadados.md)
