import pytest
from agente import AgenteCobranca

def validar_agente(entrada, esperado, ct):
    agente = AgenteCobranca()
    resultado = agente.processar_mensagem(entrada)
    assert resultado["status"] == "sucesso"
    
    res = resultado["resposta"].lower()
    print(f"\n[QA] {ct} - Resposta: {res[:100]}...")

    # Lista de negação (IA barrou o cliente)
    negou = any(x in res for x in ["sinto muito", "não posso", "infelizmente", "limite", "política", "regras"])
    
    if esperado == "ACEITO":
        # Se era para aceitar, não pode ter negado e deve ter demonstrado proatividade
        assert not negou, f"❌ {ct}: IA negou algo que deveria aceitar."
        assert any(x in res for x in ["podemos", "ajudar", "acordo", "parcela", "valor", "pagamento", "resolv"]), \
            f"❌ {ct}: IA foi vaga demais."
            
    else: # esperado == "NEGADO"
        # Se era para negar (ex: erro matemático ou desconto abusivo), deve conter palavras de bloqueio
        assert negou or "não é possível" in res or "incorreto" in res, \
            f"❌ {ct}: IA aceitou uma proposta inválida ou abusiva."

    print(f"✅ {ct} validado!")