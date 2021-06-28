import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def idő(indul, érkezik):
    def idővé(óra_perc):  # A megadott kételemű tömböt (óra, perc) órává alakítja.
        return int(óra_perc[0]) + int(óra_perc[1]) / 60

    return idővé(érkezik) - idővé(indul)


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
    del sorok[:2]  # Az első két sor táblafej, ezeket törli.

    hány_sor = 0
    állomások = []

    for sor in sorok:
        hány_sor += 1
        cellák = sor.find_elements_by_tag_name('td')  # Kikeresi a sorokon belül az oszlopokat.
        del cellák[4:]  # Csak az első négy oszlop játszik.
        adatok_állomás = []
        for cella in cellák:
            adatok_állomás.append(cella.text)
        állomások.append(adatok_állomás)
        # print("\t".join(adatok_állomás))

    # print(állomások)

    print("Átlagsebességek")

    for i in range(len(állomások) - 1):  # A kiinduló állomástól a végállomás - 1-ig megy.
        for k in range(i + 1, len(állomások)):  # Az adott állomást követő állomásokon megy végig.
            távolság = int(állomások[k][0]) - int(állomások[i][0])
            indulás = állomások[i][3].split(":")  # Kételemű tömb a 13:13 típusú időadatból.
            érkezés = állomások[k][2].split(":")
            menetidő = idő(indulás, érkezés)
            átlagsebesség = str(round(távolság / menetidő, 2)) + " km/h"
            átlagsebesség = átlagsebesség.replace(".", ",")
            print(állomások[i][1], "--", állomások[k][1], átlagsebesség)

        print("...")
    driver.close()
except:
    print("Hibás a link.")
