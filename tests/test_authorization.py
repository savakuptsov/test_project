from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utilites.config import URL

"""Авторизация с валидными данными"""

def test_auth_with_valid_data(browser):
    browser.get(URL)
    enter = MainPage(browser)
    enter.click_auth_button()

    auth = LoginPage(browser)
    auth.auth()
    auth.assert_word(auth.get_main_word, 'Личный кабинет')
    auth.assert_url('https://www.chipdip.ru/account')

    log_out = ProfilePage(browser)
    log_out.log_out()

"""Попытка авторизации с невалидными данными"""
def test_auth_with_invalid_data(browser):
    browser.get(URL)
    enter = MainPage(browser)
    enter.click_auth_button()

    auth = LoginPage(browser)
    auth.auth(email='sffsfsf@kjks.re',password='FDfdgjl45tFDd')
    auth.assert_word(auth.get_invalid_auth_label, 'Неверно указан логин или пароль, попробуйте еще раз')
    print('Сервис не авторизовал пользователя')

