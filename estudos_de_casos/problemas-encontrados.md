# Problemas e Observações Identificados

## Login sem limitação de tentativas
Foi identificado que a funcionalidade de login permite tentativas ilimitadas
de autenticação com credenciais inválidas, sem aplicação de bloqueio
ou mecanismo de proteção adicional.

Impacto potencial:
- Possibilidade de ataques de força bruta
- Comprometimento da segurança da autenticação

---

## Comportamento genérico em requisições POST na API
A API testada aceita requisições POST com payload inválido ou incompleto,
retornando resposta genérica sem validação clara.

Impacto potencial:
- Dificuldade de diagnóstico de erros de integração
- Geração de dados inconsistentes em sistemas consumidores

---

## Exposição irrestrita de dados via API
A API permite acesso a dados de usuários sem necessidade de autenticação
ou autorização.

Impacto potencial:
- Exposição de dados sensíveis
- Violação de princípios básicos de segurança da informação
