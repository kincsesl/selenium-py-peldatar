from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/kitchensink.html")

melyikid = "bmwradio"
melyikname = "multiple-select-example"
xpathja = "//button[@id='mousehover']"

try:
    q = driver.find_element_by_id(melyikid)
    q.click()
except:
    print("Nincs meg a kívánt id-jű elem: " + melyikid)
    driver.close()

try:
    q = driver.find_element_by_name(melyikname)
    q.click()
except:
    print("Nincs meg a kívánt nevű elem: " + melyikname)
    driver.close()

try:
    q = driver.find_element_by_xpath(xpathja)
    q.click()
except:
    print("Nincs meg a kívánt xpathnál levő elem: " + xpathja)
    driver.close()
