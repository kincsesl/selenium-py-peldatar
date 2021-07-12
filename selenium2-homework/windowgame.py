from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:9999/windowgame.html")

nyerő_szín = driver.find_element_by_xpath("/html/body/p[1]").text

gomblista = []

for i in range(100):
    gomblista.append(driver.find_element_by_id(i))

régi_ablak = driver.window_handles[0]
i = 0
log = False
while not log:
    gomblista[i].click()
    #time.sleep()
    új_ablak = driver.window_handles[1]
    driver.switch_to.window(új_ablak)
    szín = driver.find_element_by_tag_name("h1").text
    log = (szín == nyerő_szín) or (i > 98)
    driver.close()
    driver.switch_to.window(régi_ablak)
    i += 1

print(szín, "nyert")
driver.close()
