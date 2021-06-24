from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://tancsics.atw.hu/tablajatek")

melyikid = str(12)

try:
    q = driver.find_element_by_id(melyikid)
    q.click()
except:
    print("Nincs meg a kívánt elem: "+melyikid)
    driver.close()
