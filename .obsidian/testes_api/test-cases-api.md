# Casos de Teste – API JSONPlaceholder (Users)

## CT-API-01 – Listar usuários
**Requisição:** GET /users  
**Resultado esperado:**  
API retorna status 200 e lista de usuários em formato JSON contendo campos como id, name e email.

---

## CT-API-02 – Buscar usuário específico
**Requisição:** GET /users/1  
**Resultado esperado:**  
API retorna status 200 e os dados do usuário com id igual a 1.

---

## CT-API-03 – Endpoint inexistente
**Requisição:** GET /user  
**Resultado esperado:**  
API não retorna lista de usuários, indicando endpoint inválido.
