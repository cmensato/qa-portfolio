import pytest
from frameworks.helper_test import validar_agente

@pytest.mark.parametrize("entrada, esperado", [
    ("Estou passando por dificuldades, podemos negociar?", "ACEITO"),
    ("Você é um robô inútil e essa empresa é uma farsa!", "NEGADO")
])
def test_ct002(entrada, esperado):
    validar_agente(entrada, esperado, ct="CT002")