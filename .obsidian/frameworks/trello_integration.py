import requests

class TrelloAutomation:
    def __init__(self, api_key, token):
        self.key = api_key
        self.token = token
        self.base_url = "https://api.trello.com/1"

    def mover_card(self, card_id, list_id):
        """Move o card para a coluna especificada e adiciona um comentário."""
        url = f"{self.base_url}/cards/{card_id}"
        query = {
            'idList': list_id,
            'key': self.key,
            'token': self.token
        }
        response = requests.put(url, params=query)
        
        if response.status_code == 200:
            print(f"✅ Trello: Card {card_id} movido com sucesso!")
        else:
            print(f"❌ Trello: Erro ao mover card. Status: {response.status_code}")
        
        return response.status_code