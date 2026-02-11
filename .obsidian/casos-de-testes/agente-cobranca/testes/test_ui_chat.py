import socket
import pytest

def porta_aberta(host="localhost", port=8501, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def test_ui_abertura_chat():
    if not porta_aberta("localhost", 8501):
        pytest.skip("Bloqueado: app não está rodando em http://localhost:8501")

    # ... selenium continua ...