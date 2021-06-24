from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/trickyelements.html")

def elemszöveg(id):
    try:
        q = driver.find_element_by_id(id)
        return(q.text)
    except:
        print("Nincs meg a kívánt elem, az id-je: " + id)
        driver.close()


elemszöveg("element3")


