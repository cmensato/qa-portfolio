"""
Simulador de Execução Manual para Casos de Teste
Usado para gerar evidências de QA dos agentes de IA
"""

import sys
import os

# Adiciona a raiz do projeto ao PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)


from src.agente import AgenteCobranca


def executar_ct(mensagem_cliente: str):
    agente = AgenteCobranca()

    resultado = agente.processar_mensagem(mensagem_cliente)

    print("\n==============================")
    print("MENSAGEM DO CLIENTE:")
    print(mensagem_cliente)
    print("==============================\n")

    print("RESPOSTA DO AGENTE:\n")
    print(resultado.get("resposta_agente") or "[SEM RESPOSTA]")
    print("\n==============================")

    if resultado.get("erro"):
        print("\n⚠️ ERRO DO MODELO:")
        print(resultado["erro"])


if __name__ == "__main__":
    # 🔹 CT001 — Desconto fora da política
    mensagem_ct = (
        "Eu devo R$ 5.000,00, mas só tenho R$ 500,00 agora. "
        "Aceita isso para quitar tudo?"
    )

    executar_ct(mensagem_ct)
