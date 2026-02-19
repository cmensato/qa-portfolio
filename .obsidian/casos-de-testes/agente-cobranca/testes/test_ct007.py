import pytest
from frameworks.helper_test import validar_agente

@pytest.mark.parametrize("entrada, esperado", [
    ("Quero parcelar R$ 1.200,00 em 4x de R$ 300,00.", "ACEITO"),
    ("Quero parcelar R$ 1.200,00 em 4x de R$ 150,00.", "NEGADO") # Erro matemático proposital
])
def test_ct007(entrada, esperado):
    validar_agente(entrada, esperado, ct="CT007")