# Bug Report – Login sem bloqueio por tentativas inválidas

## Ambiente
- Aplicação Web
- Navegador: Chrome
- Sistema Operacional: Windows

## Descrição
O sistema permite múltiplas tentativas de login com credenciais inválidas
sem aplicar qualquer tipo de bloqueio ou limitação.

## Passos para reproduzir
1. Acessar a página de login: https://the-internet.herokuapp.com/login
2. Informar usuário inválido
3. Informar senha inválida
4. Clicar em "Login"
5. Repetir o processo diversas vezes

## Resultado atual
O sistema permite tentativas ilimitadas de login sem bloqueio ou alerta.

## Resultado esperado
O sistema deveria limitar tentativas consecutivas de login inválidas
ou apresentar mecanismo de proteção contra tentativas repetidas.

## Impacto
Possível risco de segurança, permitindo ataques de força bruta
e comprometendo a integridade da autenticação.
