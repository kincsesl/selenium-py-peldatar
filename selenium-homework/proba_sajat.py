from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime, date, time, timezone

mostvan = datetime.now()

options = Options()
#options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("http://users.atw.hu/vikar95/proba/")

def beír(mező, s):
    print("Id:", mező.get_attribute("id"))
    mező.send_keys(s)
    print("Érték:", mező.get_attribute("value"))


#date = driver.find_element_by_id("example-input-date")
#datetime = driver.find_element_by_id("example-input-date-time")
#datetime_local = driver.find_element_by_id("example-input-date-time-local")
month = driver.find_element_by_id("month")
week = driver.find_element_by_id("week")
#time = driver.find_element_by_id("example-input-time")

#beír(date, "002021-07-09")
#beír(datetime, "1999.08.13 12:00")
#beír(datetime_local, "002021-07-08T21:20")
beír(month, "2021\tjúnius")
beír(week, "12\t2021")
#beír(time, "21:20")



#driver.close()
