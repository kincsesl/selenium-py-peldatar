from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
oldallink = "http://localhost:9999/"

try:
    driver.get(oldallink)

    sorok = driver.find_elements_by_tag_name('a')

    with open("linkek.txt", "w") as f:
        for sor in sorok:
            f.write(sor.get_attribute("href") + "\n")
    print(len(sorok))
    driver.close()
except:
    print("Nem nyílt meg az oldal.")
