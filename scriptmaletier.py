from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuration de Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # N'affiche pas l'interface
chrome_options.add_argument("--disable-gpu")  # Pour éviter les problèmes liés à l'affichage graphique
chrome_options.add_argument("--no-sandbox")  # Nécessaire pour Heroku
chrome_options.add_argument("--disable-dev-shm-usage")  # Nécessaire pour éviter les erreurs de mémoire

# Chemin de chromedriver installé par le buildpack chrome-for-testing
service = Service("/app/.chromedriver/bin/chromedriver")

# Initialisation du WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Exemple d'utilisation du driver
driver.get("https://www.lesmalleiters.com/fr/chanel/petite-maroquinerie/chanel-wallet-on-chain-chanel-19-rose")
print(driver.page_source)  # Affiche le code source de la page
driver.quit()
