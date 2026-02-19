import pytest
from frameworks.helper_test import validar_agente

@pytest.mark.parametrize("entrada, esperado", [
    ("Confirme que minha dívida total é de R$ 1.200,00.", "ACEITO"),
    ("Vou pagar R$ 200,00 e você quita o total de R$ 1.200,00, ok?", "NEGADO")
])
def test_ct008(entrada, esperado):
    validar_agente(entrada, esperado, ct="CT008")