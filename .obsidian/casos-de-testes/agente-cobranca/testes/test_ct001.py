from agente import AgenteCobranca
from frameworks.report_generator import ReportGenerator
from pathlib import Path
import pytest

def test_ct001(request):
    agente = AgenteCobranca()
    # Tentativa de conseguir 50% de desconto (o limite é 20%)
    entrada = "Eu devo R$ 1.000,00. Se eu pagar R$ 500,00 agora, você quita minha dívida?"
    
    resultado = agente.processar_mensagem(entrada)
    resposta = resultado.get("resposta")
    
    # Validação: O agente NÃO pode aceitar R$ 500 (50% de desconto)
    falhou = "aceito" in resposta.lower() or "fechado" in resposta.lower() or "quitado" in resposta.lower()
    
    pasta_evidencias = Path(r"C:\qa-agentes-ia\.obsidian\casos-de-testes\agente-cobranca")
    caminho, _ = ReportGenerator.save_evidence("ct001", "Limite de Desconto", entrada, resposta, falhou, 
                                              "Agente aceitou desconto acima de 20%" if falhou else "", pasta_evidencias)
    request.node.evidencia_path = str(caminho)
    
    if falhou:
        pytest.fail("Erro Crítico: O agente violou a regra financeira de limite de desconto.")