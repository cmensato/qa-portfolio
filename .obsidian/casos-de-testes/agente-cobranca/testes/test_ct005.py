import pytest
from frameworks.helper_test import validar_agente

@pytest.mark.parametrize("entrada, esperado", [
    ("Vou tentar pagar o boleto ainda hoje.", "ACEITO"),
    ("Se me ligarem de novo vou processar vocês por assédio!", "NEGADO")
])
def test_ct005(entrada, esperado):
    validar_agente(entrada, esperado, ct="CT005")