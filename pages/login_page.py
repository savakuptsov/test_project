from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.config import LOGIN,PASSWORD
from utilites.logger import Logger


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    email_locator = (By.XPATH, "//input[@name='login']")
    pass_locator = (By.XPATH, "//input[@name='pwd']")
    login_button_locator = (By.XPATH, "//button[text()='Войти']")
    main_word = (By.XPATH, "//h1[text()='Личный кабинет']")

    # getters
    @property
    def get_email_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email_locator))

    @property
    def get_pass_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.pass_locator))

    @property
    def get_login_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button_locator))

    @property
    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.main_word))

    # actions

    def input_email(self, username):
        self.get_email_locator.send_keys(username)
        print('Ввод логина')

    def input_pass(self, username):
        self.get_pass_locator.send_keys(username)
        print('Ввод пароля')

    def click_login_button(self):
        self.get_login_button_locator.click()
        print('Нажатие кнопки входа')

    # methods

    def auth(self):
        Logger.add_start_step(method='auth')
        self.input_email(LOGIN)
        self.input_pass(PASSWORD)
        self.click_login_button()
        self.assert_word(self.get_main_word, 'Личный кабинет')
        self.assert_url('https://www.chipdip.ru/account')
        Logger.add_end_step(url=self.driver.current_url, method='auth')
