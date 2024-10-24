from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Options pour Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Chemins pour Chrome et Chromedriver
chrome_bin = '/app/.apt/usr/bin/google-chrome'
chromedriver_path = '/app/.chromedriver/bin/chromedriver'

chrome_options.binary_location = chrome_bin

# Utilisation du service pour chromedriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test - Aller sur un site
url = 'https://www.lesmalleiters.com/fr/chanel/petite-maroquinerie/chanel-wallet-on-chain-chanel-19-rose'
driver.get(url)

print(driver.title)
driver.quit()
