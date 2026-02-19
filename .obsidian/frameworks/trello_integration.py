import requests
from datetime import datetime

class TrelloAutomation:
    def __init__(self, api_key, token):
        self.api_key = api_key
        self.token = token
        self.base_url = "https://api.trello.com/1"
    
    def mover_card(self, card_id, coluna_id):
        url = f"{self.base_url}/cards/{card_id}"
        params = {"key": self.api_key, "token": self.token, "idList": coluna_id}
        response = requests.put(url, params=params)
        if response.status_code != 200:
            print(f"❌ Trello Erro {response.status_code}: {response.text}")
        return response.status_code == 200

    def registrar_execucao(self, card_id, status, detalhes="", caminho_evidencia=""):
        url = f"{self.base_url}/cards/{card_id}/actions/comments"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        texto = f"**[{status}]** - {timestamp}\n\n{detalhes}"
        params = {"key": self.api_key, "token": self.token, "text": texto}
        response = requests.post(url, params=params)
        return response.status_code == 200