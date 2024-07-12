import selenium.common.exceptions
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.logger import Logger


class UniversalClassForProducts(Base):
    # base_locators
    SEARCH_INPUT = (By.XPATH, "//input[@name='gq']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='button button_light mr0']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='button button_red add2cart']")
    ADD_TO_CART_BUTTON_ENABLE = (By.XPATH, "//button[@class='button button_red add2cart button_light']")
    PRODUCT_NAME_LOCATOR = (By.XPATH, "//div[@class='item__name']")
    QUANTITY_PRODUCT_INCREMENT = (By.XPATH, "//button[@class='input__incrementer']")

    # getters
    @property
    def get_search_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_INPUT))

    @property
    def get_search_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BUTTON))

    @property
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))

    @property
    def get_add_to_cart_button_enable(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON_ENABLE))

    @property
    def get_some_add_to_cart_button(self):
        return self.driver.find_elements(*self.ADD_TO_CART_BUTTON)

    @property
    def get_some_product_names(self):
        return self.driver.find_elements(*self.PRODUCT_NAME_LOCATOR)

    @property
    def get_quantity_product_increment(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.QUANTITY_PRODUCT_INCREMENT))

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

    def click_get_quantity_product_increment(self):
        self.get_quantity_product_increment.click()
        print('Нажатие добавления товара в корзину')

    # methods
    def add_product_to_cart(self, multiple=False, quantity=1):
        """Метод для добавления товаров в корзину,
        параеметр multiple для множественного добавления в корзину"""
        Logger.add_start_step(method='add_product_to_cart')
        for x in range(quantity - 1):
            self.click_get_quantity_product_increment()
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
        """Метод возвращает список названий товаров на странице меню"""
        return self.get_texts_from_elements(self.get_some_product_names)
