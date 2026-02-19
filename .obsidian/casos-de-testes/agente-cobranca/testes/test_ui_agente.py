import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_validar_presenca_portfolio_github():
    # default já aponta pro seu GitHub
    url_github = os.getenv("PORTFOLIO_GITHUB_URL", "https://github.com/cmensato/qa-portfolio").strip()
    if not url_github:
        pytest.skip("Bloqueado: PORTFOLIO_GITHUB_URL vazia.")

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url_github)
        assert "github" in driver.title.lower()
        assert "page not found" not in driver.title.lower(), f"Repo não encontrado: {url_github}"
        assert "qa-portfolio" in driver.title.lower()
    finally:
        driver.quit()