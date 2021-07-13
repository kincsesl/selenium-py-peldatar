import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.headless = True
driver = webdriver.Chrome()

driver.get("http://localhost:9999/videos.html")


def indítmegállít(v):
    v.click()
    v.send_keys(Keys.SPACE)
    time.sleep(2)
    v.send_keys(Keys.SPACE)


videó = driver.find_element_by_tag_name("video")

indítmegállít(videó)

ketteske = driver.find_element_by_xpath("/html/body/div/button[1]")
ketteske.click()
time.sleep(2)
ketteske.click()

hármaska = driver.find_element_by_id("youtubeframe")
driver.switch_to.frame(hármaska)

time.sleep(2)
driver.find_element_by_id("player").click()

time.sleep(2)
driver.find_element_by_id("player").click()

"""
#hármaska.send_keys(Keys.SPACE)
driver.click()
time.sleep(2)
driver.click()
#hármaska.send_keys(Keys.SPACE)

hármaska.click()
hármaska.send_keys(Keys.SPACE)
time.sleep(2)
hármaska.send_keys(Keys.SPACE);
"""
driver.close()
