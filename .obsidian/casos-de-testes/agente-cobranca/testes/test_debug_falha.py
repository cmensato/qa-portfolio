def test_forçar_erro_no_trello():
    """Este teste serve para validar se o card move para 'ERRO CRITICO'"""
    valor_esperado = 100
    valor_recebido = 50
    assert valor_recebido == valor_esperado, "Falha proposital para validar integração com Trello"