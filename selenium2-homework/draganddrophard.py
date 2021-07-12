import time
from selenium import webdriver
from os import getcwd
from selenium.webdriver.chrome.options import Options
from seletools.actions import drag_and_drop

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:9999/dragndrop2.html#/lists")

keret = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/ul")
források = keret.find_elements_by_tag_name("li")
cél = driver.find_element_by_id("Done")

for forrás in források:
    drag_and_drop(driver, forrás, cél)

# driver.close()
