from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
oldallink = "https://github.com/madewokherd/mines/"

driver.get(oldallink)

sorok = driver.find_element_by_tag_name("body")

kölkök = sorok.find_elements_by_xpath("/*")
for i in kölkök:
    sor = i.find_elements_by_xpath("/*")
    for elem in sor:
        print(elem.get_attribute("tagname"))

driver.close()
