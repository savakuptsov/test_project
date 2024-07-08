import time

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.classes_for_products.base_class_for_products import BaseClassForProducts
from pages.cart_page import CartPage
from utilites.config import URL

"""Выбор товара через поиск, добавление 10 экземпляров в корзину и переход к оформлению корзины """


def test_choise_1_product(browser,remove_cart):
    browser.get(URL)
    enter = MainPage(browser)
    enter.click_auth_button()

    auth = LoginPage(browser)
    auth.auth()

    select_product = ProfilePage(browser)
    select_product.product_selection('Корпусные и установочные изделия', 'Ребристые радиаторы')

    product = BaseClassForProducts(browser)
    name_product = 'HS 107-100, Радиатор 100х32х17 мм, 13 дюйм*градус/Вт'
    product.input_product(name_product)
    product.click_search_button()
    product.add_product_to_cart(quantity=10)
    product.click_cart_button()

    cart = CartPage(browser)
    time.sleep(1)
    cart.cart_submit(name_product)


"""Выбор двух товаров разных разделов через поиск, 
добавление его в корзину и переход к оформлению корзины """
def test_check_2_products(browser,remove_cart):
    browser.get(URL)

    select_product_1 = ProfilePage(browser)
    select_product_1.product_selection('Корпусные и установочные изделия', 'Ребристые радиаторы')

    product_1 = BaseClassForProducts(browser)
    name_product_1 = 'HS 107-100, Радиатор 100х32х17 мм, 13 дюйм*градус/Вт'
    product_1.input_product(name_product_1)
    product_1.click_search_button()
    product_1.click_add_to_cart_button()

    select_product_2 = ProfilePage(browser)
    select_product_2.product_selection('Оптоэлектроника', 'Светодиоды круглые')

    product_2 = BaseClassForProducts(browser)
    name_product_2 = 'GNL-3012ED, Светодиод оранжевый 60° d=3мм 8мКд 635нМ (Orange)'
    product_2.input_product(name_product_2)
    product_2.click_search_button()
    product_2.click_add_to_cart_button()
    product_2.click_cart_button()

    cart = CartPage(browser)
    cart.cart_submit(name_product_1,name_product_2)


"""Выбор 20 товаров одного подраздела, добавление в корзину и переход к оформлению корзины"""
def test_check_20_products(browser,remove_cart):
    browser.get(URL)

    select_products = ProfilePage(browser)
    select_products.product_selection('Электротехника', 'Герконы')
    products = BaseClassForProducts(browser)
    products.add_product_to_cart(multiple=True)
    name_products = products.parse_product_names()
    products.click_cart_button()
    cart = CartPage(browser)
    cart.cart_submit(*name_products)



