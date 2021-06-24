from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/general.html")

q = driver.find_elements_by_tag_name("a")

kivételek = ["https://www.w3.org/TR/html5/dom.html#phrasing-content",
             "http://www.w3schools.com/tags/", "http://example.com/",
             "https://www.fillmurray.com/", "https://creativecommons.org/licenses/by-sa/3.0",
             "https://commons.wikimedia.org/wiki/File:What_hath_God_wrought.ogg",
             "https://github.com/dbox/html5-kitchen-sink"]
#Ezeket nem fogja megnyitni

for i in q:
    print(i.text, i.get_attribute("href"), i.get_attribute("target")) #Nem nyitja meg még a külön ablakban megnyílókat sem.
    if i.get_attribute("href") not in kivételek and i.get_attribute("target") != "_blank":
        i.click()
        driver.back()
    print(i.text)
    # driver.execute_script("window.history.go(-1)")
