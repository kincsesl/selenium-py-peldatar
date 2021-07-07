import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#options.headless = True

driver = webdriver.Chrome(options=options)

driver.get("https://react-card-2a6c5.web.app/")

time.sleep(3)

gombok = driver.find_elements_by_class_name("shelf-item__buy-btn")


hány = 0
for i in gombok:
    hány += 1
    print(hány)
    i.click()

print(hány)
végösszeg = driver.find_element_by_class_name("sub-price__val")

print(végösszeg.text)

#driver.close()