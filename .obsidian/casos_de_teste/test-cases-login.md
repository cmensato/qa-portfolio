# Casos de Teste – Funcionalidade de Login

## CT-01 – Login com credenciais válidas
**Pré-condição:** Usuário cadastrado  
**Passos:**
1. Acessar a página de login
2. Informar usuário válido
3. Informar senha válida
4. Clicar em "Login"

**Resultado esperado:**  
Usuário autenticado com sucesso.

---

## CT-02 – Login com usuário inválido
**Passos:**
1. Acessar a página de login
2. Informar usuário inválido
3. Informar senha válida
4. Clicar em "Login"

**Resultado esperado:**  
Sistema exibe mensagem de erro informando falha na autenticação.

---

## CT-03 – Login com senha inválida
**Passos:**
1. Acessar a página de login
2. Informar usuário válido
3. Informar senha inválida
4. Clicar em "Login"

**Resultado esperado:**  
Sistema impede autenticação e exibe mensagem de erro.

---

## CT-04 – Login com campos vazios
**Passos:**
1. Acessar a página de login
2. Não preencher usuário e senha
3. Clicar em "Login"

**Resultado esperado:**  
Sistema deve validar campos obrigatórios e impedir o login.
