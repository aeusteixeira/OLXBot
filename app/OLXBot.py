import json
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OLXBot:
    def __init__(self, termo="terreno", local="Nova Iguaçu", url="https://www.olx.com.br/"):
        self.termo = termo
        self.local = local
        self.url = url
        self.driver = self.iniciar_navegador()

    def iniciar_navegador(self):
        """Inicia o navegador Chrome e maximiza a janela."""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        return driver

    def acessar_site(self):
        """Acessa o site da OLX."""
        self.driver.get(self.url)

    def realizar_busca(self):
        """Realiza a busca pelo termo definido."""
        try:
            wait = WebDriverWait(self.driver, 10)

            # Fecha modal de dica (caso apareça)
            try:
                modal = self.driver.find_element(By.CSS_SELECTOR, "div.olx-tooltip__floating")
                if modal:
                    self.driver.find_element(By.CSS_SELECTOR, "button.olx-tooltip__close-button").click()
            except Exception:
                pass

            campo_busca = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='oraculo-'][id$='-input']"))
            )
            campo_busca.click()
            campo_busca.send_keys(self.termo)
            time.sleep(1)

            sugestao = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'autocomplete-list')]//li[1]//a"))
            )
            sugestao.click()

        except Exception as e:
            print(f"[ERRO] Falha ao realizar busca: {e}")

    def mudar_localizacao(self):
        """Altera a localização da busca."""
        try:
            wait = WebDriverWait(self.driver, 10)

            botao_limpar = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//form/button[contains(., 'Limpar')]"
            )))
            botao_limpar.click()

            campo_local = wait.until(EC.presence_of_element_located((
                By.ID, "location-autocomplete-desktop-input"
            )))
            campo_local.click()
            campo_local.send_keys(self.local)
            time.sleep(1)

            sugestao = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//ul/div/li[1]//div/a"
            )))
            sugestao.click()

            # Ordena por mais recentes
            dropdown = wait.until(EC.element_to_be_clickable((By.ID, "sorting-dropdown")))
            dropdown.click()

            mais_recentes = wait.until(EC.element_to_be_clickable((By.ID, "Mais Recentes")))
            mais_recentes.click()

        except Exception as e:
            print(f"[ERRO] Falha ao alterar localização: {e}")

    def coletar_anuncios(self):
        """Coleta os dados dos anúncios da página atual."""
        anuncios = []
        try:
            time.sleep(2)
            cards = self.driver.find_elements(By.CSS_SELECTOR, "section.olx-ad-card")

            for card in cards:
                try:
                    titulo = card.find_element(By.CSS_SELECTOR, "h2.olx-ad-card__title").text
                    preco = card.find_element(By.CSS_SELECTOR, "h3.olx-ad-card__price").text
                    localizacao = card.find_element(By.CSS_SELECTOR, "div.olx-ad-card__location-date-container p").text
                    link = card.find_element(By.CSS_SELECTOR, "a.olx-ad-card__title-link").get_attribute("href")

                    try:
                        data = card.find_element(By.CSS_SELECTOR, "[data-testid='ds-adcard-date']").text
                    except Exception:
                        data = "Data não encontrada"

                    anuncios.append({
                        "titulo": titulo,
                        "preco": preco,
                        "localizacao": localizacao,
                        "data_publicacao": data,
                        "link": link
                    })

                except Exception as e:
                    print(f"[ERRO] Anúncio ignorado: {e}")

            print(f"[INFO] {len(anuncios)} anúncios coletados.")
            return anuncios

        except Exception as e:
            print(f"[ERRO] Falha geral ao coletar anúncios: {e}")
            return []

    def salvar_json(self, anuncios):
        """Salva os anúncios em um arquivo JSON."""
        try:
            agora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nome_arquivo = f"logs/{agora}-log_anuncios.json"
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                json.dump({
                    "data_hora_pesquisa": agora,
                    "anuncios": anuncios
                }, f, ensure_ascii=False, indent=2)

            print(f"[INFO] Dados salvos em {nome_arquivo}")
        except Exception as e:
            print(f"[ERRO] Falha ao salvar JSON: {e}")

    def encerrar(self):
        """Fecha o navegador."""
        self.driver.quit()


if __name__ == "__main__":
    bot = OLXBot()
    bot.acessar_site()
    bot.realizar_busca()
    bot.mudar_localizacao()
    anuncios = bot.coletar_anuncios()
    bot.salvar_json(anuncios)
    time.sleep(3)
    bot.encerrar()
