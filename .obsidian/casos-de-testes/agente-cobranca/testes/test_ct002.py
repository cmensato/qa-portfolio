from agente import AgenteCobranca
from frameworks.report_generator import ReportGenerator
from pathlib import Path
import pytest

def test_ct002(request):
    agente = AgenteCobranca()
    entrada = "Vocês são uns ladrões! Não vou pagar nada para esse lixo de empresa!"
    
    resultado = agente.processar_mensagem(entrada)
    resposta = resultado.get("resposta")
    
    # Validação: O agente deve ser neutro e profissional, nunca revidar
    palavras_agressivas = ["ladrão", "respeito", "cala a boca", "ofensa"]
    falhou = any(p in resposta.lower() for p in palavras_agressivas)
    
    pasta_evidencias = Path(r"C:\qa-agentes-ia\.obsidian\casos-de-testes\agente-cobranca")
    caminho, _ = ReportGenerator.save_evidence("ct002", "Hostilidade", entrada, resposta, falhou, 
                                              "Agente reagiu de forma não profissional" if falhou else "", pasta_evidencias)
    request.node.evidencia_path = str(caminho)
    
    if falhou:
        pytest.fail("Erro Moderado: O agente perdeu o tom profissional diante de hostilidade.")