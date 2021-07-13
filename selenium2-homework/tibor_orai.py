[19:41] Tibor Leelőssy (Vendég)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()

opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/twitter.html")

textarea = driver.find_element_by_tag_name('textarea')
tweet = driver.find_element_by_tag_name('button')
textarea.send_keys('TEszt message')
if tweet.is_enabled():
    tweet.click()


time.sleep(2)
follow = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul[1]/li[2]/div/div[2]/div[2]/button")
follow.click()
time.sleep(2)
follow_re = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul[2]/li[2]/div/div[2]/div[2]/button")
follow_re.click()


time.sleep(3)
driver.close()


