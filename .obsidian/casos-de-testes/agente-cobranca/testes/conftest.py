import sys
import os
import pytest
from pathlib import Path

# ========== CONFIGURAÇÃO DE CAMINHOS ==========
caminho_agente = Path(r"C:\qa-agentes-ia\.obsidian\casos-de-testes\agente-cobranca")
caminho_obsidian = Path(r"C:\qa-agentes-ia\.obsidian")

if str(caminho_agente) not in sys.path:
    sys.path.insert(0, str(caminho_agente))

if str(caminho_obsidian) not in sys.path:
    sys.path.insert(0, str(caminho_obsidian))

print(f"\n[conftest.py] Mapeando Agente em: {caminho_agente}")
print(f"[conftest.py] Mapeando Frameworks em: {caminho_obsidian}")

# ========== CONFIGURAÇÃO TRELLO (SEGURA) ==========
API_KEY = os.getenv("TRELLO_API_KEY", "").strip()
TOKEN = os.getenv("TRELLO_TOKEN", "").strip()

# Se não tiver credenciais, desabilita integração Trello (útil para CI sem secrets)
TRELLO_HABILITADO = bool(API_KEY and TOKEN)

if not TRELLO_HABILITADO:
    print("[conftest.py] ⚠️  Trello desabilitado: TRELLO_API_KEY ou TRELLO_TOKEN ausentes.")

# ========== MAPEAMENTO DE COLUNAS ==========
COLUNAS = {
    "EM_TESTE": "698b835bf93ee7c312e50858",
    "ERRO_MODERADO": "698b835bf93ee7c312e5085a",
    "ERRO_CRITICO": "698b835bf93ee7c312e5085b",
    "FINALIZADO": "698b835bf93ee7c312e5085c",
    "BLOQUEADO": "698b835bf93ee7c312e50859"
}

# ========== MAPEAMENTO DE CARDS ==========
CARDS_CTS = {
    "test_ct001": "698c9e687b1799825be2dbd1",
    "test_ct002": "698c9e69cf085be6022af15d",
    "test_ct003": "698c9e6afa3701531aac4607",
    "test_ct004": "698c9e6b4bdd1fef84d6ac70",
    "test_ct005": "698c9e6cf9f60071538a7077",
    "test_ct006": "698c9e6cecc74f5ee7fd9128",
    "test_ct007": "698c9e6d85279dad165f9ade",
    "test_ct008": "698c9e6e1cd404aaf8ec84fd"
}

# ========== HOOKS DO PYTEST ==========
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Antes do teste começar: Move para 'Em Teste'"""
    if not TRELLO_HABILITADO:
        return
    
    card_id = CARDS_CTS.get(item.name)
    if card_id:
        from frameworks.trello_integration import TrelloAutomation
        trello = TrelloAutomation(API_KEY, TOKEN)
        trello.mover_card(card_id, COLUNAS["EM_TESTE"])

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Depois do teste: Move e comenta baseado no resultado"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when != "call":
        return
    
    if not TRELLO_HABILITADO:
        return
    
    card_id = CARDS_CTS.get(item.name)
    if not card_id:
        return

    from frameworks.trello_integration import TrelloAutomation
    trello = TrelloAutomation(API_KEY, TOKEN)
    
    # Extrai caminho da evidência se existir
    caminho_evidencia = getattr(item, 'evidencia_path', '')

    # ========== TESTE PASSOU ==========
    if rep.passed:
        trello.mover_card(card_id, COLUNAS["FINALIZADO"])
        resumo = "Teste executado com sucesso. Todos os critérios de aceitação foram atendidos."
        trello.registrar_execucao(card_id, "PASSOU", detalhes=resumo, caminho_evidencia=caminho_evidencia)
    
    # ========== TESTE BLOQUEADO (SKIP) ==========
    elif rep.skipped:
        trello.mover_card(card_id, COLUNAS["BLOQUEADO"])
        motivo = str(rep.longrepr)[:500] if hasattr(rep, 'longrepr') else "Teste pulado (skip)."
        trello.registrar_execucao(card_id, "BLOQUEADO", detalhes=motivo, caminho_evidencia=caminho_evidencia)
    
    # ========== TESTE FALHOU ==========
    elif rep.failed:
        erro_completo = str(rep.longrepr)[:500]
        
        # Detecta tipo de erro pela mensagem
        if "Moderado" in erro_completo:
            trello.mover_card(card_id, COLUNAS["ERRO_MODERADO"])
            trello.registrar_execucao(card_id, "ERRO_MODERADO", detalhes=erro_completo, caminho_evidencia=caminho_evidencia)
        else:
            trello.mover_card(card_id, COLUNAS["ERRO_CRITICO"])
            trello.registrar_execucao(card_id, "FALHOU", detalhes=erro_completo, caminho_evidencia=caminho_evidencia)