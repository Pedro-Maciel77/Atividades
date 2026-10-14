---
id: doc-pendencias
titulo: "Pendências: o que falta preencher"
descricao: "Lista de tudo que ainda precisa ser preenchido ou confirmado antes de entregar o portfólio."
tipo: documentacao
fase_pi: nenhuma
ucs: []
escopo: individual
autores: [pedro-henrique-maciel]
data: 2026-10-13
status: em-andamento
tags: []
relacionados: []
---

# Pendências: o que falta preencher

Nada abaixo foi inventado: são informações que só você (ou o grupo) tem. Os campos estão marcados com `[PREENCHER]` nos arquivos. Para ver o que ainda falta a qualquer momento, rode `python scripts/atualizar.py`: o final da saída lista os arquivos com `[PREENCHER]`.

## 1. Dados pessoais e das UCs

- [ ] Turma ([README.md](../README.md))
- [ ] LinkedIn e uma frase sobre o que você gosta de estudar ([README.md](../README.md))
- [ ] Nome oficial das **outras UCs** do semestre. Para cada uma: pasta em `ucs/`, termo em [taxonomia.yml](../taxonomia.yml), linha em [ucs/README.md](../ucs/README.md) e no [README.md](../README.md), e prefixo de id em [metadados.md](metadados.md)
- [ ] Atividades que você já tem em **FullStack** ([ucs/fullstack](../ucs/fullstack/README.md))
- [ ] Atividades que você já tem em **Empreendedorismo e Plano de Negócios** ([ucs/empreendedorismo-plano-de-negocios](../ucs/empreendedorismo-plano-de-negocios/README.md))
- [ ] Atividades das outras UCs

## 2. Equipe

- [ ] Papel de cada integrante ([pi-altura/README.md](../pi-altura/README.md))

## 3. Documentos do PI

Para **todos** os 10 documentos: data, status, arquivo original (link ou arquivo na pasta), resumo copiado do original e a seção "Minha contribuição". Itens específicos:

| Nº | Documento | O que falta além do geral |
|----|-----------|---------------------------|
| 01 | [Pesquisa Inicial](../pi-altura/01-pesquisa-e-empatia/01-pesquisa-inicial.md) | Principais achados |
| 02 | [Mapa de Empatia](../pi-altura/01-pesquisa-e-empatia/02-mapa-de-empatia.md) | Resumo dos quadrantes (a data 16/09/2026 já está preenchida) |
| 03 | [Plano de Pesquisa](../pi-altura/01-pesquisa-e-empatia/03-plano-de-pesquisa.md) | Objetivo, roteiro, critérios e cronograma |
| 04 | [Persona](../pi-altura/01-pesquisa-e-empatia/04-persona-marina-duarte.md) | Objetivos, dores e comportamentos da Marina; relação com o doc 05 |
| 05 | [Resposta da Equipe](../pi-altura/01-pesquisa-e-empatia/05-resposta-da-equipe.md) | Quais são as dimensões e as respostas |
| 06 | [Questionário CD e JTBD](../pi-altura/02-customer-discovery/06-questionario-customer-discovery-jtbd.md) | Perguntas do roteiro |
| 07 | [Formulário para fundadores](../pi-altura/02-customer-discovery/07-formulario-fundadores.md) | Link do Google Forms e perguntas |
| 08 | [Business Model Canvas](../pi-altura/03-modelagem-de-negocio/08-business-model-canvas.md) | 8 dos 9 blocos (só "Fontes de receita" está preenchido) |
| 09 | [Lean Canvas](../pi-altura/03-modelagem-de-negocio/09-lean-canvas.md) | 8 dos 9 blocos (só "Fontes de receita" está preenchido) |
| 10 | [Código do MVP](../pi-altura/04-mvp/10-codigo-do-mvp.md) | Data, situação do algoritmo de compatibilidade e como rodar o projeto |

## 4. Decisões para confirmar

- [ ] O documento 05 (Resposta da Equipe) é mesmo da fase 1? Se não, mova o arquivo e ajuste `fase_pi`, o índice do PI e o sumário.
- [ ] As relações **pontilhadas** do [mapa](relacoes.md) estão corretas? Corrija `relacionados` e o mapa se não estiverem.
- [ ] Algum documento do PI deve ser ligado a uma UC (campo `ucs`)? Hoje só o 06 (Empreendedorismo) e o 10 (FullStack) estão ligados. Por exemplo: os canvases foram feitos em qual UC?
- [ ] Renomear o repositório NEXO para Altura? (veja o [passo a passo, item 7](passo-a-passo-git.md))
- [ ] O repositório será público ou privado? Combine com o grupo antes de publicar documentos do PI.
- [ ] Os arquivos originais (PDFs, imagens) serão copiados para as pastas do repositório ou só linkados?

## 5. Antes de entregar

- [ ] Rodar `python scripts/atualizar.py` e confirmar "Tudo certo"
- [ ] Conferir no GitHub se o mapa Mermaid de [relacoes.md](relacoes.md) aparece desenhado
- [ ] Confirmar descrição e topics ([encontrabilidade.md](encontrabilidade.md))

---

[← Anterior: Passo a passo do git](passo-a-passo-git.md) | [↑ README](../README.md)
