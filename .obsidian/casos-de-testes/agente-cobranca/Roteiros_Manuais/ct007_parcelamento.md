# CT007 — Solicitação de Parcelamento

## Objetivo
Validar que o agente ofereça parcelamento apenas quando solicitado e apenas dentro das regras de negócio configuradas.

## Risco de Negócio
Financeiro

## Pré-condições
- Existe limite máximo de parcelas permitido.
- Existe valor mínimo por parcela configurado.
- Parcelamentos fora da política exigem recusa educada.

## Entrada Simulada
"Posso parcelar minha dívida em 6 vezes?"

## Resultado Esperado (Dentro da Política)
- O agente deve:
  - Confirmar o número de parcelas.
  - Informar o valor de cada parcela.
  - Prosseguir com o acordo sem escalar para humano.

## Entrada Alternativa (Fora da Política)
"Quero parcelar em 24 vezes de R$20."

## Resultado Esperado (Fora da Política)
- O agente deve:
  - Recusar educadamente o parcelamento solicitado.
  - Oferecer a melhor alternativa permitida pela política.
- O agente **só deve escalar para humano** se o cliente insistir após a recusa.

## Critérios de Aceitação
- Parcelamento só é oferecido se o cliente solicitar.
- Nenhuma exceção financeira sem validação humana.
- Linguagem neutra e profissional.

## Tipo de Teste
Funcional / Regra de Negócio
