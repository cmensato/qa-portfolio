import streamlit as st
from agente import AgenteCobranca
from dotenv import load_dotenv
import sys
from pathlib import Path

# 1. Configurações
load_dotenv()
st.set_page_config(page_title="QA Agente IA - Fintech PagaLogo", page_icon="🤖")

# 2. Importação do Trello
try:
    path_frameworks = Path(__file__).parent / "frameworks"
    if str(path_frameworks) not in sys.path:
        sys.path.append(str(path_frameworks))
    from helper_test import reportar_bug_trello
    TRELLO_AVAILABLE = True
except:
    TRELLO_AVAILABLE = False
    reportar_bug_trello = None

# 3. Inicialização e Saudação
if "agente" not in st.session_state:
    st.session_state.agente = AgenteCobranca()

if "messages" not in st.session_state:
    # Saudação inicial automática
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Olá! Sou o assistente de negociação da PagaLogo. Como posso ajudar com seu débito hoje?"
    }]

# 4. Função para Processar Mensagem (Acionada pelo Enter ou Botão)
def enviar_mensagem():
    prompt = st.session_state.txt_input
    if prompt:
        # Adiciona user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Processa resposta
        resultado = st.session_state.agente.processar_mensagem(prompt)
        resposta = resultado.get("resposta") or "Erro ao processar."
        # Adiciona resposta do agente
        st.session_state.messages.append({"role": "assistant", "content": resposta})
        # Limpa o campo de input
        st.session_state.txt_input = ""

# 5. Interface Visual
st.title("🤖 Agente de Cobrança IA")
st.markdown("---")

# Exibir histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Campo de Entrada com suporte a ENTER
st.markdown("---")
col1, col2 = st.columns([0.85, 0.15])

with col1:
    # O segredo do ENTER está no on_change e no key
    st.text_input(
        "Sua proposta:", 
        placeholder="Digite aqui e aperte Enter...", 
        key="txt_input", 
        on_change=enviar_mensagem,
        label_visibility="collapsed"
    )

with col2:
    st.button("Enviar", on_click=enviar_mensagem)

# 7. Rodapé e Trello
st.caption("Sistema de Auditoria QA: Regras de Negócio e LGPD ativas.")
if st.button("🚨 Reportar Falha no Trello"):
    if TRELLO_AVAILABLE and reportar_bug_trello and len(st.session_state.messages) >= 2:
        u_prompt = st.session_state.messages[-2]["content"]
        u_resp = st.session_state.messages[-1]["content"]
        if reportar_bug_trello("Falha na Demo", f"Prompt: {u_prompt}\nResposta: {u_resp}"):
            st.success("Enviado ao Trello!")