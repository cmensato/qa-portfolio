# Abordagem de Testes

A abordagem adotada seguiu uma lógica progressiva, iniciando por testes exploratórios
para entendimento do comportamento do sistema, seguida pela formalização dos cenários
em casos de teste estruturados.

Para a aplicação Web, o foco foi compreender o fluxo de autenticação,
as mensagens retornadas ao usuário e possíveis riscos associados
a tentativas repetidas de login.

Nos testes de API, foram realizadas requisições manuais utilizando navegador
e ferramenta Postman, validando status HTTP, estrutura das respostas
e comportamento diante de cenários inválidos.

A análise de segurança teve como objetivo identificar comportamentos
que, em ambientes reais, poderiam representar riscos ao negócio
ou à integridade das informações.
