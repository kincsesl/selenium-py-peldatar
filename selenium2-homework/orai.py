from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)
from selenium.webdriver.common.keys import Keys

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/twitter.html#")

for i in range(4):
    csoport = driver.find_element_by_xpath("//div[@class = 'pb-10 text-center']")
    linkek = csoport.find_elements_by_tag_name("a")
    print(linkek[i].get_attribute("href"))
    linkek[i].click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

driver.close()
