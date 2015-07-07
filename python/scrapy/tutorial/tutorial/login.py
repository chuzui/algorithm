from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.rijksmuseum.nl/en/'

driver = webdriver.Firefox()
driver.get(url)
print driver.title

