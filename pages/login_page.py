from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.config import LOGIN,PASSWORD
from utilites.logger import Logger


class LoginPage(Base):

    # locators
    EMAIL_LOCATOR = (By.XPATH, "//input[@name='login']")
    PASS_LOCATOR = (By.XPATH, "//input[@name='pwd']")
    LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Войти']")
    MAIN_WORD = (By.XPATH, "//h1[text()='Личный кабинет']")
    INVALID_AUTH_LABEL = (By.XPATH, "//span[@class='with-icon with-icon_attention_red redtext']")

    # getters
    @property
    def get_email_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.EMAIL_LOCATOR))

    @property
    def get_pass_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PASS_LOCATOR))

    @property
    def get_login_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON_LOCATOR))

    @property
    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MAIN_WORD))

    @property
    def get_invalid_auth_label(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.INVALID_AUTH_LABEL))

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

    def auth(self,email=LOGIN,password=PASSWORD):
        """Метод авторизации пользователя"""
        Logger.add_start_step(method='auth')
        self.input_email(email)
        self.input_pass(password)
        self.click_login_button()
        Logger.add_end_step(url=self.driver.current_url, method='auth')
