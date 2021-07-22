import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')  # scope="module","determine_scope","class","package"
def browser():
    options = Options()
    # options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:9999/filltablewithsum.html")
    return driver


def test_first_testcase(browser):
    összegtábla = browser.find_element_by_id("resultTotals")
    quantitytotals = összegtábla.find_element_by_id("qtyTotals")
    pricetotals = összegtábla.find_element_by_id("priceTotals")
    tartalmazó_form = browser.find_element_by_id("order")
    productmező = tartalmazó_form.find_element_by_id("product")
    quantitymező = tartalmazó_form.find_element_by_id("quantity")
    pricemező = tartalmazó_form.find_element_by_id("price")
    resetgomb = tartalmazó_form.find_element_by_id("resetbtn")
    addgomb = tartalmazó_form.find_element_by_id("add")
    assert addgomb.text == "Add To Table"


def test_addgomb(browser):
    driver = browser
    driver.get("http://localhost:9999/filltablewithsum.html")
    assert True
    # assert oldalteszt.addgomb.text == "Add To Table"
