import time

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.classes_for_products.base_class_for_products import BaseClassForProducts
from pages.cart_page import CartPage
from utilites.config import URL

"""Авторизация с валидными данными"""

def test_auth_with_valid_data(browser):
    browser.get(URL)
    enter = MainPage(browser)
    enter.click_auth_button()

    auth = LoginPage(browser)
    auth.auth()

    log_out = ProfilePage(browser)
    log_out.log_out()

"""Попытка авторизации с невалидными данными"""
def test_auth_with_invalid_data(browser):
    browser.get(URL)
    enter = MainPage(browser)
    enter.click_auth_button()

    auth = LoginPage(browser)
    auth.auth(email='sffsfsf@kjks.re',password='FDfdgjl45tFDd')

