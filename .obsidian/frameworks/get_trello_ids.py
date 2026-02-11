import os
import requests

KEY = os.getenv( "TRELLO_API_KEY" )
TOKEN = os.getenv( "TRELLO_TOKEN" )
BOARD_URL = "https://trello.com/b/xtOcggjJ/qa-para-agentes-de-ia-cobranca"

# Extrai o ID curto do board da URL
board_id = BOARD_URL.split('/')[-2]

url = f"https://api.trello.com/1/boards/{board_id}/lists"
query = {'key': KEY, 'token': TOKEN}

response = requests.get(url, params=query)
lists = response.json()

print("\n--- IDs DAS SUAS COLUNAS ---")
for l in lists:
    print(f"Coluna: {l['name']} | ID: {l['id']}")