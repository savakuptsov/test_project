import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utilites.config import URL
from selenium.webdriver.common.by import By
from base.base_class import Base
from pages.cart_page import CartPage
from utilites.config import PATH_TO_DRIVER

@pytest.fixture(scope="session")
def browser():
    o = Options()
    o.add_experimental_option("detach", True)
    s = Service(PATH_TO_DRIVER)
    driver = webdriver.Chrome(options=o, service=s)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def remove_cart(browser):
    yield
    print('\nЗапуск очистки корзины:')
    cart = Base(browser)
    cart.click_cart_button()
    clearcart = CartPage(browser)
    clearcart.clear_cart()




