from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:9999/alert_playground.html")

alertgomb = driver.find_element_by_xpath("/html/body/div/div[2]/input[1]")
confirmgomb = driver.find_element_by_xpath("/html/body/div/div[2]/input[2]")
promptgomb = driver.find_element_by_xpath("/html/body/div/div[2]/input[3]")
beírt_szöveg = driver.find_element_by_id("demo")
duplakatt = driver.find_element_by_id("double-click")

szöveg = "Bármit is írsz..."

try:
    alertgomb.click()
    alertablak = driver.switch_to.alert
    if alertablak.text == "I am alert":
        alertablak.accept()
        print("Az alertablak oké.")
    else:
        print("Az alert nem oké.")
    confirmgomb.click()
    confirmablak = driver.switch_to.alert
    if confirmablak.text == "I am confirm":
        confirmablak.accept()
        print("A confirm oké.")
    else:
        print("A confirm nem oké.")
    promptgomb.click()
    promptablak = driver.switch_to.alert
    promptablak.send_keys(szöveg)
    promptablak.accept()
    if beírt_szöveg.text == "You entered: " + szöveg:
        print("Promptablak oké.")
    else:
        print("Promptablak nem oké.")

    actionChains = ActionChains(driver)
    actionChains.double_click(duplakatt).perform()
    duplakattablak = driver.switch_to.alert
    if duplakattablak.text == "You double clicked me!!!, You got to be kidding me":
        confirmablak.accept()
        print("A duplakatt is oké.")
    else:
        print("A duplakatt nem oké.")
# except:
# print("Valami nem jó.")
finally:
    driver.close()
