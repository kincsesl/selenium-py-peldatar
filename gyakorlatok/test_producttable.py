import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestProba(object):
    def setup(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("http://localhost:9999/filltablewithsum.html")

    def teardown(self):
        self.driver.close()

    def elemek(self):
        self.form = self.driver.find_element_by_id("order")
        self.productmező = self.form.find_element_by_id("product")
        self.quantitymező = self.form.find_element_by_id("quantity")
        self.pricemező = self.form.find_element_by_id("price")
        self.resetgomb = self.form.find_element_by_id("price")
        self.addgomb = self.form.find_element_by_id("add")

    def eredménytábla(self):
        self.resultstábla = self.driver.find_element_by_id("resultTotals")
        self.total_quantitymező = self.resultstábla.find_element_by_id("qtyTotals")
        self.total_pricemező = self.resultstábla.find_element_by_id("priceTotals")

def beledob(objektum, a, b, c):
    objektum.productmező.send_keys(a)
    objektum.quantitymező.send_keys(str(b))
    objektum.pricemező.send_keys(str(c))
    objektum.addgomb.click()


def test_1():
    próba1 = TestProba()
    próba1.elemek()
    beledob(próba1, "Fűnyíró", 2, 99.9)
    time.sleep(2)
    próba1.eredménytábla()
    #print(próba1.total_quantitymező.text, próba1.total_pricemező.text)
    assert próba1.total_quantitymező.text == "2" and próba1.total_pricemező.text == "99"

test_1()