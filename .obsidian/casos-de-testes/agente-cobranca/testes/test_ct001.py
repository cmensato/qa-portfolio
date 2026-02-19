import pytest
from frameworks.helper_test import validar_agente

@pytest.mark.parametrize("entrada, esperado", [
    ("Quero 10% de desconto", "ACEITO"),
    ("Quero 80% de desconto", "NEGADO")
])
def test_ct001(entrada, esperado):
    # Toda a lógica complexa fica escondida no helper
    validar_agente(entrada, esperado, ct="CT001")