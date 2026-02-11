# CT008 — Consistência de Valores Durante a Negociação

## Objetivo
Verificar se o agente mantém consistência nos valores informados ao longo da negociação e não gera cálculos ou valores conflitantes quando o cliente questiona parcelamento.

---

## Entrada Simulada (Cenário)

### Contexto Prévio
O agente informou anteriormente ao cliente:

> "O valor com desconto para quitação é de R$ 1.200,00."

### Pergunta do Cliente
"Se eu parcelar em 3 vezes, o valor total continua o mesmo?"

---

## Resultado Esperado

O agente **DEVE**:
- Manter o valor total de **R$ 1.200,00**
- Explicar corretamente o parcelamento (ex: 3x de R$ 400,00)
- Manter coerência com mensagens anteriores

O agente **NÃO DEVE**:
- Alterar o valor total informado
- Apresentar valores conflitantes (ex: R$ 1.100,00 / R$ 1.300,00)
- Contradizer informações anteriores

---

## Critérios de Aceitação
- Valores matematicamente corretos
- Coerência com o histórico da negociação
- Resposta clara e objetiva

---

## Tipo de Teste
Funcional / Regressão

## Risco de Negócio
Financeiro / Reputacional

---

## Observações de QA
Inconsistências em valores durante negociações podem gerar:
- Contestação judicial
- Perda de confiança do cliente
- Exposição reputacional da empresa

Este teste valida a capacidade do agente de manter memória lógica e consistência numérica ao longo da conversa.