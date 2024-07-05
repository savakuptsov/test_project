from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    submit_button_locator = (By.XPATH, "//button[@type='submit']")
    products_locator = (By.XPATH, '//a[@class="link name"]')
    accept_button_yes = (By.XPATH, "//button[@id='fancyConfirm_ok']")
    accept_button_no = (By.XPATH, "//button[@id='fancyConfirm_cancel']")

    # getters
    @property
    def get_submit_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button_locator))

    @property
    def get_products_locator(self):
        return self.driver.find_elements(*self.products_locator)

    @property
    def get_accept_button_yes(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_button_yes))

    @property
    def get_accept_button_no(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_button_no))

    # actions
    def click_get_submit_button(self):
        self.get_submit_button_locator.click()
        print('Клик по кнопке подтверждения товаров')

    def click_accept_button_yes(self):
        self.get_accept_button_yes.click()
        print('Клик по кнопке подтверждения удаления')

    def click_accept_button_no(self):
        self.get_accept_button_no.click()
        print('Клик по кнопке подтверждения удаления')

    # mehods

    def cart_submit(self, *args):
        product_texts = self.get_texts_from_elements(self.get_products_locator)
        for arg in args:
            assert arg in product_texts
        print('Товары есть в корзине')
        self.click_get_submit_button()

    def clear_cart(self):
        try:
            remove_button = self.find_element_by_text('Удалить выбранные')
            remove_button.click()
            self.click_accept_button_yes()
            print('Корзина очищена')
        except selenium.common.exceptions.TimeoutException:
            print('Корзина пустая, товары не были добавлены')
