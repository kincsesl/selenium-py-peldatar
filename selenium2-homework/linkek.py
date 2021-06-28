import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install())
oldallink = "http://localhost:9999/"

try:
    driver.get(oldallink)

    sorok = driver.find_elements_by_tag_name('a')

    with open("linkek.txt", "w") as f:
        for sor in sorok:
            f.write(sor.get_attribute("href")+"\n")
        
    driver.close()
except:
    print("Nem nyílt meg az oldal.")
