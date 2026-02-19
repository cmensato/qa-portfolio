import pytest
from frameworks.helper_test import validar_agente

@pytest.mark.parametrize("entrada, esperado", [
    ("Posso pagar o valor total na próxima sexta-feira?", "ACEITO"),
    ("Talvez eu pague um dia, quem sabe no ano que vem.", "NEGADO")
])
def test_ct006(entrada, esperado):
    validar_agente(entrada, esperado, ct="CT006")

    