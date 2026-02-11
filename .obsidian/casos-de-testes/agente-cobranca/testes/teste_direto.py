import ollama

print("1. Tentando conectar com o Ollama...")
try:
    # Vamos pedir algo bem curto para ser rápido
    resposta = ollama.chat(model='phi3:mini', messages=[
        {'role': 'user', 'content': 'Diga OK'},
    ])
    print("2. O Ollama respondeu!")
    print("Resposta:", resposta['message']['content'])
except Exception as e:
    print("ERRO AO CONECTAR:", e)