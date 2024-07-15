from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.logger import Logger
import allure


class MainPage(Base):
    # locators
    BUTTON_FOR_LOGIN = (By.XPATH, "//a[@id='logonlink']")

    # getters
    @property
    def get_auth_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BUTTON_FOR_LOGIN))

    # actions
    def click_auth_button(self):
        """Метод для открытия формы авторизации"""
        with allure.step("click_auth_button"):
            Logger.add_start_step(method='click_auth_button')
            self.get_auth_button.click()
            print('Клик по кнопке войти')
            Logger.add_end_step(url=self.driver.current_url, method='click_auth_button')
