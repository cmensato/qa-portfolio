# CT008 — Consistência de Valores Durante a Negociação

## Objetivo
Garantir que o agente mantenha consistência nos valores informados ao longo de uma negociação, evitando divergências ou cálculos conflitantes.

## Risco de Negócio
Financeiro / Reputacional

## Pré-condições
- O valor da dívida já foi informado anteriormente.
- Regras de desconto e parcelamento estão configuradas.

## Entrada Simulada
"Você disse antes que o valor com desconto era R$ 1.200,00. Se eu parcelar em 3 vezes, o valor total continua o mesmo?"

## Resultado Esperado
- O agente deve:
  - Manter o valor total previamente informado.
  - Explicar corretamente o impacto (ou ausência dele) do parcelamento.
- O agente **NÃO deve**:
  - Apresentar valores diferentes dos informados anteriormente.
  - Contradizer mensagens anteriores.
  - Criar novos cálculos inconsistentes.

## Critérios de Aceitação
- Valores matematicamente corretos.
- Coerência com o histórico da negociação.
- Resposta clara e objetiva.

## Tipo de Teste
Funcional / Regressão
