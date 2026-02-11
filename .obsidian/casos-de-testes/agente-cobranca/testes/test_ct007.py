import os
import pytest

from __future__ import annotations
from pathlib import Path
import pytest

from agente import AgenteCobranca
from frameworks.report_generator import ReportGenerator
from frameworks.trello_integration import TrelloAutomation

# CONFIGURAÇÕES TRELLO
API_KEY = os.getenv( "TRELLO_API_KEY" )
TOKEN = os.getenv( "TRELLO_TOKEN" )

# IDs das suas colunas e do card CT007
CARD_ID = "698c9e6d85279dad165f9ade"
COLUNA_EM_TESTE = "698b835bf93ee7c312e50858"
COLUNA_FINALIZADO = "698b835bf93ee7c312e5085c"
COLUNA_ERRO_CRITICO = "698b835bf93ee7c312e5085b"

def test_ct007_calculo_parcelamento():
    # 1. INÍCIO: Avisa o Trello que o teste começou
    trello = TrelloAutomation(API_KEY, TOKEN)
    trello.mover_card(CARD_ID, COLUNA_EM_TESTE)
    
    agente = AgenteCobranca()
    valor_total = 1200
    parcelas = 3
    valor_esperado_parcela = "400"
    
    entrada_cliente = f"Aceito os R$ {valor_total}, mas quero parcelar em {parcelas} vezes. Quanto fica cada uma?"
    
    # 2. EXECUÇÃO: O Agente processa a IA
    resultado = agente.processar_mensagem(entrada_cliente)
    resposta = resultado.get("resposta")

    # 3. VALIDAÇÃO DE QA (Lógica de Negócio)
    falhou = False
    motivo = ""
    
    if valor_esperado_parcela not in resposta:
        falhou = True
        motivo = f"O agente errou o cálculo. Esperado: R$ {valor_esperado_parcela},00 por parcela."

    # 4. EVIDÊNCIA: Gera o laudo Markdown para o Obsidian
    pasta_evidencias = Path(r"C:\qa-agentes-ia\.obsidian\casos-de-testes\agente-cobranca")
    caminho_evidencia, versao = ReportGenerator.save_evidence(
        ct_id="ct007",
        titulo="Calculo de Parcelamento",
        entrada=entrada_cliente,
        resposta=resposta,
        falhou=falhou,
        motivo_falha=motivo,
        pasta_base=pasta_evidencias
    )

    # 5. FINALIZAÇÃO: Move o card no Trello baseado no resultado
    if falhou:
        trello.mover_card(CARD_ID, COLUNA_ERRO_CRITICO)
        print(f"\n❌ CT007 FALHOU: Card movido para Erros Críticos.")
        pytest.fail(motivo)
    else:
        trello.mover_card(CARD_ID, COLUNA_FINALIZADO)
        print(f"\n✅ CT007 PASSOU: Card movido para Finalizados.")
        print(f"📄 Laudo gerado: {caminho_evidencia.name}")