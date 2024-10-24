from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Chemin vers ChromeDriver et Chrome installés via le buildpack
chrome_driver_path = "/app/.chromedriver/bin/chromedriver"
chrome_binary_path = "/app/.apt/usr/bin/google-chrome-stable"

# Configurer les options Chrome pour Heroku
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path
chrome_options.add_argument('--headless')  # Mode sans interface graphique
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialisation du driver Chrome
print("Initialisation du driver Chrome...")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL de la page produit
url = 'https://www.lesmalleiters.com/fr/chanel/petite-maroquinerie/chanel-wallet-on-chain-chanel-19-rose'
print(f"Accès à l'URL : {url}")
driver.get(url)

# Attendre que l'élément soit visible
wait = WebDriverWait(driver, 10)

try:
    # Extraire le nom du sac
    print("Extraction du nom du sac...")
    nom_sac = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.keepEditorStyle'))).text
    print(f"Nom du sac: {nom_sac}")
    
    # Extraire le prix
    print("Extraction du prix...")
    prix = driver.find_element(By.CSS_SELECTOR, 'span.price').text
    print(f"Prix: {prix}")

    # Extraire la description
    print("Extraction de la description...")
    description = driver.find_element(By.CSS_SELECTOR, 'div.p-description').text
    print(f"Description: {description}")

except Exception as e:
    print(f"Erreur lors de l'extraction des données : {str(e)}")

# Fermer le WebDriver
driver.quit()
print("Fin du scraping.")
