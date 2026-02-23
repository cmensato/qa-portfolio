import os
from datetime import datetime

def gerar_evidencia(nome_teste, input_cliente, output_agente, status, analise):
    # 1. Garante que a pasta existe
    if not os.path.exists("evidencias"):
        os.makedirs("evidencias")

    # 2. Lógica de Versionamento (v1, v2, v3...)
    # O nome do arquivo será apenas: nome_do_teste_vX.md
    versao = 1
    while True:
        nome_arquivo = f"evidencias/{nome_teste}_v{versao}.md"
        if not os.path.exists(nome_arquivo):
            break
        versao += 1

    # 3. Prepara os dados internos
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_emoji = "✅ PASSED" if status == "PASSED" else "❌ FAILED"

    # 4. Monta o conteúdo do Markdown
    linhas = [
        f"# Evidência de Teste de IA - {nome_teste.upper()}",
        "",
        f"**Versão:** v{versao}",
        f"**Data/Hora:** {data_hora}",
        f"**Status:** {status_emoji}",
        "",
        "---",
        "",
        "## 📥 Input do Cliente",
        "```text",
        input_cliente,
        "```",
        "",
        "## 🤖 Output do Agente",
        "```text",
        output_agente,
        "```",
        "",
        "## 🔍 Análise de QA",
        analise,
        "",
        "---",
        f"*Evidência v{versao} gerada automaticamente pelo Framework de QA*"
    ]

    # 5. Salva o arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print(f"📄 Arquivo de evidência criado com sucesso: {nome_arquivo}")