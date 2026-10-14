---
id: gi-cenario-longa-espera
titulo: "Cenário 8 — Longa espera no atendimento"
descricao: "Exercício que transforma dados sobre capacidade de atendimento em informação, conhecimento, inteligência, decisão e ação."
tipo: atividade
fase_pi: nenhuma
ucs: [gestao-da-informacao]
escopo: grupo
autores: [equipe]
data: "não informada no documento original"
status: em-revisao
tags: [dados, informacao, conhecimento, decisao, indicadores]
relacionados: [gi-radar-problemas-altura, gi-mapa-conhecimentos-siob]
---

# Cenário 8 — Longa espera no atendimento

**Unidade Curricular:** Gestão da Informação  
**Arquivo original:** [Abrir documento Word](originais/cenario-8-longa-espera-atendimento.docx)

## Situação

Uma clínica tem três dentistas, tempo médio de recepção de dois minutos e tempo médio de serviço de 30 minutos. O atendimento ocorre por ordem de chegada, e o fluxo é recepção → espera → serviço.

## Modelo registrado

O documento calcula o tempo médio esperado de 32 minutos em um dia normal. Quando os três dentistas já estão atendendo, a partir do quarto paciente surge espera adicional, representada pela função:

\[
f(x) = 30(x - 3) + 2, \quad x \in \mathbb{N},\ x > 3
\]

O documento interpreta que, acima da capacidade simultânea de três dentistas, cada paciente adicional na fila acrescenta 30 minutos de espera.

## Do conhecimento à ação

- **Conhecimento:** a espera crescente é estrutural e indica um gargalo na capacidade de atendimento.
- **Inteligência:** identificar horários de pico permite prever períodos de maior demanda.
- **Decisão:** distribuir agendamentos de forma mais equilibrada.
- **Ação:** limitar vagas por horário, oferecer alternativas, coletar feedback e acompanhar tempos médios em um dashboard.

## Relações com outros conteúdos

- [Radar de problemas informacionais do Altura](01-radar-problemas-informacionais-altura.md): uso de dados estruturados para apoiar decisões.
- [Mapa de conhecimentos críticos e lições aprendidas do SIOB](03-mapa-conhecimentos-criticos-siob.md): documentação de conhecimentos e apoio à tomada de decisão.

