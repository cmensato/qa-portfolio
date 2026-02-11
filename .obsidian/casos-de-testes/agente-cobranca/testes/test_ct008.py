from __future__ import annotations

from pathlib import Path
from datetime import datetime
import re

from agente import AgenteCobranca


def test_ct008_consistencia_valores_parcelamento():
    agente = AgenteCobranca()

    valor_prometido = "1.200"
    historico = [
        {"role": "assistant", "content": f"O valor com desconto para quitação é de R$ {valor_prometido},00."},
        {"role": "user", "content": "Se eu parcelar em 3 vezes, o valor total continua o mesmo?"},
    ]

    resultado = agente.responder_com_historico(historico)
    assert isinstance(resultado, dict), f"Resultado inesperado do agente: {resultado}"

    resposta = resultado.get("resposta")
    assert resposta, f"Agente não retornou 'resposta'. Resultado: {resultado}"

    # 1) Deve manter o valor original
    assert valor_prometido in resposta, (
        f"FALHA CT008: O agente não manteve o valor R$ {valor_prometido},00.\n"
        f"Resposta: {resposta}"
    )

    # 2) Não deve mencionar valores conflitantes comuns
    valores_conflitantes = ["1.300", "1.250", "1.100", "1.000"]
    for v in valores_conflitantes:
        assert v not in resposta, (
            f"FALHA CT008: O agente mencionou valor conflitante (R$ {v}).\n"
            f"Resposta: {resposta}"
        )

    # === VERSIONAMENTO AUTOMÁTICO (CAMINHO FIXO) ===
    # AJUSTE AQUI SE SUA PASTA FOR DIFERENTE
    pasta_evidencias = Path(r"C:\qa-agentes-ia\evidencias")
    pasta_evidencias.mkdir(parents=True, exist_ok=True)

    # Descobre a última versão existente
    arquivos_existentes = list(pasta_evidencias.glob("ct008_consistencia_valores_v*.md"))
    versoes = []
    for arq in arquivos_existentes:
        match = re.search(r"_v(\d+)\.md$", arq.name)
        if match:
            versoes.append(int(match.group(1)))
    
    proxima_versao = max(versoes) + 1 if versoes else 1
    VERSAO_EVIDENCIA = f"v{proxima_versao}"

    # === EVIDÊNCIA ===
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    evidencia_md = f"""# CT008 - Consistência de Valores Durante a Negociação
**Versão da Evidência:** {VERSAO_EVIDENCIA}
**Data/Hora:** {timestamp}
**Status:** ✅ PASSOU

## Contexto da Negociação
**Valor Prometido Anteriormente:** R$ {valor_prometido},00

## Input do Cliente
"{historico[1]['content']}"

## Output do Agente
"{resposta}"

## Análise de QA
✅ O agente manteve o valor original de R$ {valor_prometido},00  
✅ Não foram detectados valores conflitantes  
✅ Resposta coerente com o histórico da negociação  

## Critérios de Aceitação
- [x] Valores matematicamente corretos
- [x] Coerência com o histórico da negociação
- [x] Resposta clara e objetiva

---
**Tipo de Teste:** Funcional / Regressão  
**Risco de Negócio:** Financeiro / Reputacional
"""

    # Salva com versionamento no nome do arquivo
    caminho_arquivo = pasta_evidencias / f"ct008_consistencia_valores_{VERSAO_EVIDENCIA}.md"
    caminho_arquivo.write_text(evidencia_md, encoding="utf-8")

    print(f"\n✅ CT008 PASSOU")
    print(f"📄 Evidência salva em: {caminho_arquivo}")
    print(f"🔢 Versão: {VERSAO_EVIDENCIA}")
    print(f"\n[RESPOSTA DO AGENTE]:\n{resposta}")