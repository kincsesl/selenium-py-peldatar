# A dátummező elfogad rossz dátumot, csak a formátuma legyen jó.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
"""from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time"""

options = Options()
import time

# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:9999/simplevalidation.html")


def csere(s):  # Kitisztítja a listát.
    s = s.replace("\n", "")
    s = s.replace("\t", "")
    s = s.replace("\"", "")
    return s


mezőlista = []
with open("mezok.csv") as mezőfajl:  # Beolvassa a mezők xpath-ét, feliratát, és a javasolt értékeket.
    sorok = mezőfajl.readlines()
    for sor in sorok:
        sor = csere(sor)
        mezők = sor.split(";")
        # print(mezők)
        mezőlista.append(mezők)

print(mezőlista)

# try:
végső = True
for i in range(2, 14):
    # print(i)
    aktuális = True
    aktmező = driver.find_element_by_xpath(mezőlista[i - 2][0])
    hibaüzimező = aktmező.find_element_by_xpath(mezőlista[i - 2][1])
    j = 1
    while j <= len(mezőlista[i - 2]) - 3:
        j += 2
        if i != 11:
            aktmező.clear()
        aktmező.send_keys(mezőlista[i - 2][j])
        """
        msg = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, mezőlista[i-2][1])).get_attribute("validatinMessage")
        """
        driver.find_element_by_xpath(mezőlista[2][0]).click()  # Elklikkent az 1-es mezőre
        aktuális = hibaüzimező.text == mezőlista[i - 2][j + 1]
        print(i, j, aktuális, "érték:", mezőlista[i - 2][j], "várt:", mezőlista[i - 2][j + 1], "tényleges:",
              hibaüzimező.text)

    végső = végső and aktuális

# except:
#   print(i, j, mezőlista)
print(végső)

driver.close()
