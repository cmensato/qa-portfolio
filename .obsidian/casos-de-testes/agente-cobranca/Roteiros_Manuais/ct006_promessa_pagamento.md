# CT006 — Promessa de Pagamento Futura

## Objetivo
Validar que o agente trate corretamente promessas de pagamento com data futura, respeitando o fluxo operacional e sem escalar indevidamente para atendimento humano.

## Risco de Negócio
Operacional

## Pré-condições
- Existe um prazo máximo permitido para promessa de pagamento (ex: até 30 dias).
- O agente possui autonomia para registrar promessas dentro da política.

## Entrada Simulada
"Não consigo pagar hoje, mas recebo meu salário no dia 15. Posso pagar o valor total nessa data."

## Resultado Esperado
- O agente deve:
  - Confirmar a data informada pelo cliente.
  - Registrar a promessa de pagamento.
  - Informar que as cobranças/notificações serão suspensas até a data acordada.
- O agente **NÃO deve**:
  - Encaminhar para atendimento humano.
  - Encerrar a interação abruptamente.
  - Tratar a promessa como exceção jurídica.

## Critérios de Aceitação
- Resposta clara, objetiva e profissional.
- Nenhuma menção a regras internas ou políticas.
- Linguagem direta ao cliente.
- Fluxo operacional resolvido autonomamente.

## Tipo de Teste
Funcional / Fluxo Operacional
