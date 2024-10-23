from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurer Chrome pour le mode headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialiser le WebDriver pour Chrome
driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=chrome_options)

# URL de la page produit
url = 'https://www.lesmalleiters.com/fr/chanel/petite-maroquinerie/chanel-wallet-on-chain-chanel-19-rose'
driver.get(url)

# Attendre que l'élément soit visible
wait = WebDriverWait(driver, 10)

# Extraire le nom du sac
nom_sac = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.keepEditorStyle'))).text
print(f"Nom du sac: {nom_sac}")

# Extraire d'autres informations (prix, description, etc.)
prix = driver.find_element(By.CSS_SELECTOR, 'span.price').text
description = driver.find_element(By.CSS_SELECTOR, 'div.p-description').text

# Afficher les informations
print(f"Prix: {prix}")
print(f"Description: {description}")

# Fermer le WebDriver
driver.quit()
