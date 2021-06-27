import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install())
oldallink = input("Írd be a vonat menetrendjének a linkjét [Üres inputnál én választok]: ")
if oldallink == "":
    oldallink = "https://elvira.mav-start.hu/elvira.dll/x/vt?v=6748&d=21.06.28&language=1&ed=60D60793"
try:
    driver.get(oldallink)

    sorok = driver.find_elements_by_tag_name('tr')
    del sorok[:2]

    hány_sor = 0
    állomások = []

    for sor in sorok:
        hány_sor += 1
        cellák = sor.find_elements_by_tag_name('td')
        del cellák[4:]
        adatok_állomás = []
        for cella in cellák:
            adatok_állomás.append(cella.text)
        állomások.append(adatok_állomás)
        # print("\t".join(adatok_állomás))

    # print(állomások)

    print("Átlagsebességek")

    for i in range(len(állomások) - 1):
        for k in range(i + 1, len(állomások)):
            távolság = int(állomások[k][0]) - int(állomások[i][0])
            indulás = állomások[i][3].split(":")
            érkezés = állomások[k][2].split(":")
            indulási_idő = int(indulás[0]) + int(indulás[1]) / 60
            érkezési_idő = int(érkezés[0]) + int(érkezés[1]) / 60
            átlagsebesség = str(round(távolság / (érkezési_idő - indulási_idő), 2)) + " km/h"
            átlagsebesség = átlagsebesség.replace(".", ",")
            print(állomások[i][1], "-", állomások[k][1], átlagsebesség)

        print("...")
    driver.close()
except:
    print("Hibás a link.")