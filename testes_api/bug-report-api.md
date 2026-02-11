# Bug Report – API aceita método POST sem validação adequada

## Endpoint
POST https://jsonplaceholder.typicode.com/users

## Descrição
A API aceita requisições POST com payload vazio ou inválido,
retornando resposta genérica sem indicar erro ou validação de dados.

## Passos para reproduzir
1. Abrir o Postman
2. Criar requisição POST para /users
3. Enviar payload vazio ou incompleto
4. Executar a requisição

## Resultado atual
API retorna resposta genérica, sem validação clara ou mensagem de erro.

## Resultado esperado
API deveria validar dados de entrada e retornar erro apropriado
ou mensagem clara de uso incorreto.

## Impacto
Pode mascarar falhas de integração, gerar dados inconsistentes
e dificultar diagnóstico de erros por consumidores da API.
