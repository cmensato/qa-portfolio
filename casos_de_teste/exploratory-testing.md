# Teste Exploratório – Funcionalidade de Login

## Sistema testado
Site de testes: https://the-internet.herokuapp.com/login

## Objetivo do teste
Avaliar o comportamento da funcionalidade de login diante de credenciais válidas e inválidas,
observando mensagens de retorno, validações e possíveis riscos funcionais e de segurança.

## Abordagem
Foram realizados testes exploratórios considerando os seguintes cenários:
- acesso inicial à página de login
- tentativa de login com campos vazios
- tentativa de login com credenciais inválidas
- análise das mensagens retornadas pelo sistema
- repetição de tentativas de autenticação

## Observações
- Ao acessar a página de login, o sistema apresenta um alerta informativo relacionado
à alteração de senha, caracterizando um comportamento esperado da aplicação.
- Em tentativas de login com credenciais inválidas, o sistema retorna mensagem de erro adequada,
informando falha na autenticação.
- Não foi identificado bloqueio ou limitação após múltiplas tentativas consecutivas de login inválido.

## Conclusão
A funcionalidade de login apresenta mensagens claras ao usuário em caso de erro,
porém permite tentativas ilimitadas de autenticação sem mecanismos de proteção adicionais.
Em um cenário real, esse comportamento pode representar risco de segurança,
possibilitando ataques de força bruta.
