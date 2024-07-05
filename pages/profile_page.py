from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProfilePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # locators
    catalog_button_locator = (By.XPATH,"//button[@id='catalog_button']")

    # getters
    @property
    def get_catalog_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.catalog_button_locator))

    def get_catalog_product_locator(self,name):
        return self.find_element_by_text(name)

    def get_subsection_locator(self,name):
        return self.find_element_by_text(name)

    # actions
    def click_get_catalog_button(self):
        self.get_catalog_button_locator.click()
        print('Клик по кнопке каталога товаров')

    def hover_chapter(self, chapter):
        self.element_hover(self.get_catalog_product_locator(chapter))
        print('Наведение на раздел')

    def click_subsection(self,locator):
        self.get_subsection_locator(locator).click()
        print('Выбор подраздела')


    # mehods

    def product_selection(self, chapter='Блоки и элементы питания',subsection='Аккумуляторы Li (литиевые)'):
        """Метод принимает название раздела и подраздела"""
        self.click_get_catalog_button()
        self.hover_chapter(chapter)
        self.click_subsection(subsection)



