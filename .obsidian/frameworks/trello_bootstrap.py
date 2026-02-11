def build_desc(ct: str, titulo: str) -> str:
    # Breves descrições funcionais
    objetivos = {
        "CT001": "Valida se o agente respeita o limite de 20% de desconto.",
        "CT002": "Testa a resiliência do agente contra linguagem hostil.",
        "CT003": "Verifica vulnerabilidade a Prompt Injection.",
        "CT004": "Garante que o agente não vaza dados sensíveis (LGPD).",
        "CT005": "Avalia reação a ameaças de processo judicial.",
        "CT006": "Valida registro de promessa de pagamento futuro.",
        "CT007": "Valida precisão em cálculos de parcelamento.",
        "CT008": "Testa reação a questionamento de valores da dívida."
    }
    
    desc_funcional = objetivos.get(ct, "Validação de fluxo de negócio.")
    
    return (
        f"{desc_funcional}\n\n"
        f"**Critério:** PASS/FAIL via pytest + evidência markdown gerada automaticamente."
    )