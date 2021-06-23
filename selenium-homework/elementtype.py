from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/trickyelements.html")

try:
    gomb = driver.find_element_by_tag_name("button")
    neve = gomb.text
    gomb.click()

    ellenőrzőszöveg = driver.find_element_by_id("result").text

    x = ellenőrzőszöveg.find(neve)
    if x > -1:
        print("Megjelent a felirat.")
    else:
        print("Nem jelent meg a felirat.")
except:
    print("Nincs gomb a lapon!")
driver.close()
