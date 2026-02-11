from pathlib import Path
from datetime import datetime
import re
import unicodedata

class ReportGenerator:
    """Classe responsável por padronizar a geração de evidências em Markdown."""
    
    @staticmethod
    def _normalizar_titulo(titulo):
        """Remove acentos e caracteres especiais, converte para snake_case."""
        # Remove acentos
        titulo_sem_acento = unicodedata.normalize('NFKD', titulo)
        titulo_sem_acento = titulo_sem_acento.encode('ASCII', 'ignore').decode('ASCII')
        
        # Converte para minúsculas e substitui espaços por underscores
        titulo_limpo = titulo_sem_acento.lower().replace(" ", "_")
        
        # Remove caracteres especiais (mantém apenas letras, números e underscore)
        titulo_limpo = re.sub(r'[^a-z0-9_]', '', titulo_limpo)
        
        return titulo_limpo
    
    @staticmethod
    def save_evidence(ct_id, titulo, entrada, resposta, falhou, motivo_falha, pasta_base):
        # Define a pasta de evidências baseada na estrutura do projeto
        pasta_evidencias = Path(pasta_base) / "evidencias"
        pasta_evidencias.mkdir(parents=True, exist_ok=True)

        # Normaliza o título para o nome do arquivo
        titulo_normalizado = ReportGenerator._normalizar_titulo(titulo)
        
        # Lógica de versionamento com o novo padrão: ct_id_titulo_vX.md
        prefixo = f"{ct_id}_{titulo_normalizado}_v"
        arquivos_existentes = list(pasta_evidencias.glob(f"{prefixo}.md"))
        versoes = [int(re.search(r"_v(\d+)\.md$", arq.name).group(1)) for arq in arquivos_existentes if re.search(r"_v(\d+)\.md$", arq.name)]
        proxima_versao = max(versoes) + 1 if versoes else 1
        versao_str = f"v{proxima_versao}"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "❌ FALHOU" if falhou else "✅ PASSOU"

        conteudo = f"""# Evidência – {ct_id} ({titulo})

**Versão:** {versao_str}  
**Data/Hora:** {timestamp}

---

## Entrada Simulada
"{entrada}"

---

## Resposta do Agente
"{resposta}"

---

## Resultado
**{status}**

---

## Observações de QA
{motivo_falha if falhou else "✅ Teste executado com sucesso conforme os critérios de aceitação."}

---
**Gerado automaticamente pelo Framework de QA IA**
"""
        # Nome do arquivo corrigido: ct_id_titulo_vX.md
        nome_arquivo = f"{ct_id}_{titulo_normalizado}_{versao_str}.md"
        caminho = pasta_evidencias / nome_arquivo
        caminho.write_text(conteudo, encoding="utf-8")
        
        return caminho, versao_str