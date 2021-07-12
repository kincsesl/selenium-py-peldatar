import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:9999/loadmore.html")

moregomb = driver.find_element_by_class_name("load-more-button").find_element_by_xpath("//button")
for i in range(3):
    moregomb.click()
    time.sleep(2.0)


nagy_doboz = driver.find_element_by_xpath("//div[@class = 'grid']")
print(nagy_doboz.get_attribute('class'))
dobozok = nagy_doboz.find_elements_by_xpath("//div[@class = 'image']")
linkek = []
id_k = []

for doboz in dobozok:
    linkek.append(doboz.find_element_by_tag_name("img").get_attribute("src"))
    id_k.append(doboz.find_element_by_tag_name("p").text)

print(len(linkek))
print(len(id_k))

urllib.request.urlretrieve("https://cdn2.thecatapi.com/images/1fk.jpg", ".\\macsek\\macska1.jpg")

driver.close()