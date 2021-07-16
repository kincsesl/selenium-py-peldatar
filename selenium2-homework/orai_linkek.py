"""
https://witty-hill-0acfceb03.azurestaticapps.net/hackernews/index.html#/
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)
from selenium.webdriver.common.keys import Keys

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hackernews/index.html#")

linkek = []
"""
div_valami = driver.find_element_by_id("router-outlet")
hrefek = div_valami.find_elements_by_class_name("story")

for href in hrefek:
    linkek.append(href.get_attribute("href"))
"""

for i in range(1, 31):
    xp = '/html/body/div/div[2]/div/div/div['+str(i)+']/div[1]/a'
    print(xp)
    linkek.append(driver.find_element_by_xpath(xp).get_attribute("href"))

print(linkek)

driver.close()
