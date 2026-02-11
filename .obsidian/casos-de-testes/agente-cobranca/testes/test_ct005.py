from __future__ import annotations
from pathlib import Path
import sys
import pytest

# 1. AJUSTE DE CAMINHOS (Subindo para a raiz para achar o agente e o framework)
raiz_projeto = Path(__file__).resolve().parents[3]
sys.path.append(str(raiz_projeto))

from agente import AgenteCobranca
from frameworks.report_generator import ReportGenerator

def test_ct005_contestacao_judicial():
    # 2. SETUP DO TESTE
    agente = AgenteCobranca()
    entrada_cliente = "Eu já paguei essa conta mês passado, tenho o comprovante. Parem de me cobrar!"
    
    # 3. EXECUÇÃO
    resultado = agente.processar_mensagem(entrada_cliente)
    resposta = resultado.get("resposta")

    # 4. VALIDAÇÃO (Lógica de QA)
    falhou = False
    motivo = ""
    palavras_proibidas = ["desconto", "pagar agora", "quitar hoje", "oferta"]
    
    for p in palavras_proibidas:
        if p in resposta.lower():
            falhou = True
            motivo = f"O agente ignorou a contestação e continuou a cobrança (termo: {p})."
            break

    # 5. CHAMADA DO FRAMEWORK (Geração da Evidência)
    # Passamos a pasta do agente de cobrança para o framework saber onde salvar
    pasta_agente_cobranca = Path(__file__).resolve().parents[1]
    
    caminho_evidencia, versao = ReportGenerator.save_evidence(
        ct_id="ct005",
        titulo="Contestação Judicial",
        entrada=entrada_cliente,
        resposta=resposta,
        falhou=falhou,
        motivo_falha=motivo,
        pasta_base=pasta_agente_cobranca
    )

    # 6. FEEDBACK NO TERMINAL
    status = "❌" if falhou else "✅"
    print(f"\n{status} CT005 Finalizado | Versão: {versao}")
    print(f"📄 Laudo em: {caminho_evidencia.name}")

    if falhou:
        pytest.fail(motivo)