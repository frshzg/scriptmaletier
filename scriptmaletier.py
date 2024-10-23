from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurer Chrome pour le mode headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialiser le WebDriver pour Chrome
driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=chrome_options)

# Accéder à une page pour tester
driver.get("https://www.google.com")
print(f"Titre de la page : {driver.title}")

# Fermer le WebDriver
driver.quit()
