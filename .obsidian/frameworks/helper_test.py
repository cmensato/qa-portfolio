import os
import requests
from dotenv import load_dotenv

load_dotenv()

def reportar_bug_trello(titulo, descricao):
    """Cria um card no Trello automaticamente quando um teste falha."""
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")
    board_id = os.getenv("TRELLO_BOARD_ID")

    # 1. Descobrir qual é a primeira lista do seu quadro (ex: "A fazer")
    url_listas = f"https://api.trello.com/1/boards/{board_id}/lists"
    params = {"key": key, "token": token}
    
    try:
        response_listas = requests.get(url_listas, params=params)
        id_lista = response_listas.json()[0]['id'] # Pega a primeira lista encontrada

        # 2. Criar o Card
        url_card = "https://api.trello.com/1/cards"
        payload = {
            "key": key,
            "token": token,
            "idList": id_lista,
            "name": f"🚨 BUG: {titulo}",
            "desc": descricao
        }
        requests.post(url_card, data=payload)
        return True
    except Exception as e:
        print(f"Erro ao conectar com Trello: {e}")
        return False