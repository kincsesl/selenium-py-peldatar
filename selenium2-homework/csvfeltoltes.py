import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:9999/another_form.html")


def formaz(dátum):
    d1 = dátum[0:4]
    d2 = dátum[4:6]
    d3 = dátum[6:8]
    return d1 + "-" + d2 + "-" + d3


with open("table_in2.csv", "r") as csvfile_alap:
    sorok = csvfile_alap.readlines()
    for egysor in sorok:
        egysor = egysor.replace("\n", "")
        sor = egysor.split(",")
        name = driver.find_element_by_id("fullname")
        name.clear()
        name.send_keys(sor[0])
        email = driver.find_element_by_id("email")
        email.clear()
        email.send_keys(sor[1])
        dob = driver.find_element_by_id("dob")
        dob.clear()
        dob.send_keys(sor[2])
        phone = driver.find_element_by_id("phone")
        phone.clear()
        phone.send_keys(sor[3])
        küldésgomb = driver.find_element_by_id("submit")
        küldésgomb.click()

exportgomb = driver.find_element_by_xpath("/html/body/main/div/button")
exportgomb.click()
time.sleep(2.0)


def összehasonlít(a, b):
    if (a == b):
        print("Minden oké.")
    else:
        for i in range((b)):
            print("Sorok:", a[i], b[i])


with open("C:\\Users\\Valaki\\Downloads\\table.csv", "r") as letöltött:
    with open("table_in2.csv", "r") as alap:
        csvreader_letöltött = letöltött.readlines()
        csvreader_alap = alap.readlines()
        összehasonlít(csvreader_alap, csvreader_letöltött)

driver.close()
