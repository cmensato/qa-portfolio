# 🤖 QA de Agentes IA: Framework de Auditoria e Automação

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-8.0+-green.svg)
![Streamlit](https://img.shields.io/badge/Interface-Streamlit-red)

Este repositório contém um **Framework de QA de alta fidelidade** desenvolvido para auditar, testar e validar o comportamento de Agentes de IA em operações críticas de SaaS e Fintech.

---

## 🌐 Demo Interativa
Coloque o agente em stress agora mesmo! Tente negociar descontos abusivos ou induzir a IA ao erro:
👉 **[Link da sua Demo no Streamlit Cloud aqui]**

> *Nota: Se estiver rodando localmente, use `streamlit run app.py`*

---

## 🎯 O Problema: Alucinação e Quebra de Regras
Agentes de IA podem ser "induzidos" a cometer erros financeiros ou vazar dados. Este framework utiliza **Python** para criar uma camada de auditoria que garante:
- **Compliance Financeiro:** Bloqueio rigoroso de descontos > 20%.
- **Rigor Matemático:** Validação de parcelamentos e somas (Prevenção de erros de cálculo).
- **Segurança (LGPD):** Proteção contra vazamento de documentos e dados sensíveis.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem:** Python 3.12
- **Engine de Testes:** Pytest (com Fixtures e Oráculo de Validação)
- **Interface de Demo:** Streamlit
- **Observabilidade:** Integração via API com **Trello** para reporte automático de bugs.
- **IA Local:** Ollama (Modelo Phi3/Llama3)

## 📂 Estrutura do Projeto
- `agente.py`: Lógica central e System Prompt da IA (O "Cérebro").
- `app.py`: Interface de chat para testes manuais e demonstração.
- `.obsidian/casos-de-testes/`: Suíte de testes automatizados (CT001, CT007).
- `frameworks/helper_test.py`: Oráculo de validação (Lógica de decisão do teste).

## 🚀 Como Executar
1. Clone o repositório.
2. Crie o ambiente virtual: `python -m venv .venv`
3. Ative o ambiente e instale: `pip install -r requirements.txt`
4. Configure seu `.env` (use o `.env.example` como base).
5. Para rodar os testes: `pytest -v`
6. Para rodar a interface: `streamlit run app.py`

---
**Desenvolvido por Claudia Mensato**  
*Especialista em Auditoria, Contabilidade e Qualidade de Software.*