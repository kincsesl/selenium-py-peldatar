from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)
from selenium.webdriver.common.keys import Keys

driver.get("http://localhost:9999/scrolltoload.html")

html = driver.find_element_by_tag_name("html")


def lapozz():
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)


for i in range(2):
    lapozz()


def görögj():
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute(js)


# görögj()

képek = driver.find_elements_by_tag_name("img")
id_i = driver.find_elements_by_tag_name("p")

id_k = []
html_ek = []

for id in id_i:
    id_k.append(id.text)

for kép in képek:
    html_ek.append(kép.get_attribute("src"))

print(html_ek)
print(id_k)
driver.close()
