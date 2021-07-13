import shutil

import requests
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
fájlnevek = []

for id in id_i:
    id_k.append(id.text)

for kép in képek:
    html_ek.append(kép.get_attribute("src"))
    fájlnevek.append("macsek\\"+kép.get_attribute("src")[34:])
print(html_ek)
print(id_k)

for i in range(20):
    r = requests.get(html_ek[i])
    #id_je = id_k[i].replace("Cat id: ", "")
    if r.status_code == 200:
        with open(fájlnevek[i], "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    i += 1
driver.close()
