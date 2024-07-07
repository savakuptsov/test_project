import selenium.common.exceptions
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.logger import Logger

class BaseClassForProducts(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # base_locators
    search_input = (By.XPATH, "//input[@name='gq']")
    search_button = (By.XPATH, "//button[@class='button button_light mr0']")
    add_to_cart_button = (By.XPATH, "//button[@class='button button_red add2cart']")
    add_to_cart_button_enable = (By.XPATH, "//button[@class='button button_red add2cart button_light']")
    product_name_locator = (By.XPATH, "//div[@class='item__name']")

    # getters
    @property
    def get_search_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_input))

    @property
    def get_search_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button))

    @property
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.add_to_cart_button))

    @property
    def get_add_to_cart_button_enable(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_button_enable))

    @property
    def get_some_add_to_cart_button(self):
        return self.driver.find_elements(*self.add_to_cart_button)

    @property
    def get_some_product_names(self):
        return self.driver.find_elements(*self.product_name_locator)

    # actions
    def input_product(self, product):
        self.get_search_input.send_keys(product)
        print('Ввод название товара в строку поиску')

    def click_search_button(self):
        self.get_search_button.click()
        print('Нажатие кнопки поиска товара')

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button.click()
        print('Нажатие добавления товара в корзину')

    # methods
    def add_product_to_cart(self,multiple=False):
        """Метод для добавления товаров в корзину,
        параеметр multiple для множественного добавления в корзину"""
        Logger.add_start_step(method='add_product_to_cart')
        if multiple:
            try:
                for x in self.get_some_add_to_cart_button:
                    x.click()
            except selenium.common.exceptions.TimeoutException:
                print('Товар уже в корзине')
        else:
            try:
                self.click_add_to_cart_button()
            except selenium.common.exceptions.TimeoutException:
                print('Товар уже в корзине')
        Logger.add_end_step(url=self.driver.current_url, method='add_product_to_cart')

    def parse_product_names(self):
        return self.get_texts_from_elements(self.get_some_product_names)


