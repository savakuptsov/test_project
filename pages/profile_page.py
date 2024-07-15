from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.logger import Logger
import allure


class ProfilePage(Base):
    # locators
    CATALOG_BUTTON_LOCATOR = (By.XPATH, "//button[@id='catalog_button']")

    # getters
    @property
    def get_catalog_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATALOG_BUTTON_LOCATOR))

    def get_catalog_product_locator(self, name):
        return self.find_element_by_text(name)

    def get_subsection_locator(self, name):
        return self.find_element_by_text(name)

    @property
    def get_exit_locator(self):
        return self.find_element_by_text('Выход')

    # actions
    def click_get_catalog_button(self):
        self.get_catalog_button_locator.click()
        print('Клик по кнопке каталога товаров')

    def hover_chapter(self, chapter):
        self.element_hover(self.get_catalog_product_locator(chapter))
        print('Наведение на раздел')

    def click_subsection(self, locator):
        self.get_subsection_locator(locator).click()
        print('Выбор подраздела')

    def click_exit(self):
        self.get_exit_locator.click()
        print('Выход из аккаунта')

    # methods

    def product_selection(self, chapter='Блоки и элементы питания', subsection='Аккумуляторы Li (литиевые)'):
        """Метод для выбора подраздела товаров, принимает название раздела и подраздела"""
        with allure.step("click_auth_button"):
            Logger.add_start_step(method='product_selection')
            self.click_get_catalog_button()
            self.hover_chapter(chapter)
            self.click_subsection(subsection)
            Logger.add_end_step(url=self.driver.current_url, method='product_selection')

    def log_out(self):
        """Метод деавторизации"""
        with allure.step("click_auth_button"):
            Logger.add_start_step(method='product_selection')
            self.click_exit()
            self.assert_url('https://www.chipdip.ru/account/logon?ReturnUrl=%2faccount')
            Logger.add_end_step(url=self.driver.current_url, method='product_selection')
