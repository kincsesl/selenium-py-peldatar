from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:9999/pagination.html")

adataink = []
a_betűsek = []

kulcsok = driver.find_elements_by_tag_name("th")

tovább = driver.find_element_by_id("next")
while True:
    sorok = driver.find_elements_by_xpath("//tr[@class = 'ng-scope']")
    for sor in sorok:
        szótár = {}
        cellák = sor.find_elements_by_tag_name("td")
        i = 0
        for cella in cellák:
            szótár[kulcsok[i].text] = cella.text
            i += 1
        adataink.append(szótár)
        if szótár[kulcsok[1].text][0] == "A":
            a_betűsek.append(szótár)
    tovább = driver.find_element_by_id("next")
    if tovább.is_enabled():
        tovább.click()
    else:
        break

print(adataink)

for i in a_betűsek:
    print(i["First name"])

with open("egycsvfile.csv", "w") as file:
    sor1 = ""
    for kulcs in kulcsok:
        sor1 += kulcs.text + ";"
    file.write(sor1)
    for adatsor in adataink:
        file.write("\n")
        sor = ""
        for kulcs in kulcsok:
            sor += adatsor[kulcs.text] + ";"
        sor = ascii(sor).replace("'", "")
        file.write(sor)
driver.close()
