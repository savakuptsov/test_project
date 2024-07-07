from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # locators
    button_for_login = (By.XPATH,"//a[@id='logonlink']")

    # getters
    @property
    def get_auth_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_for_login))

    # actions
    def click_auth_button(self):
        """Метод для открытия формы авторизации"""
        Logger.add_start_step(method='click_auth_button')
        self.get_auth_button.click()
        print('Клик по кнопке войти')
        Logger.add_end_step(url=self.driver.current_url, method='click_auth_button')


