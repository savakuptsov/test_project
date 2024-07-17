from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from utilites.logger import Logger
import allure


class CartPage(Base):
    # locators
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//button[@class='button button_red button_big button_w100 not-print']")
    PRODUCTS_LOCATOR = (By.XPATH, '//a[@class="link name"]')
    ACCEPT_BUTTON_YES = (By.XPATH, "//button[@id='fancyConfirm_ok']")
    ACCEPT_BUTTON_NO = (By.XPATH, "//button[@id='fancyConfirm_cancel']")
    EMPTY_CART_LOCATOR = (By.XPATH, "//div[@id='cart_empty']/h3")

    # getters
    @property
    def get_submit_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON_LOCATOR))

    @property
    def get_products_locator(self):
        self.driver.implicitly_wait(2)
        return self.driver.find_elements(*self.PRODUCTS_LOCATOR)

    @property
    def get_accept_button_yes(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ACCEPT_BUTTON_YES))

    @property
    def get_accept_button_no(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ACCEPT_BUTTON_NO))

    @property
    def get_empty_cart_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.EMPTY_CART_LOCATOR))

    # actions
    def click_submit_button(self):
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
        """Метод для проверки корзины и подтверждения"""
        with allure.step("cart_submit"):
            Logger.add_start_step(method='auth')
            product_texts = self.get_texts_from_elements(self.get_products_locator)
            for arg in args:
                assert arg in product_texts
            print('Товары есть в корзине')
            self.click_submit_button()
            self.assert_url('https://www.chipdip.ru/order/form?from=cart')

    def clear_cart(self):
        """Метод для очистки корзины"""
        with allure.step("clear_cart"):
            Logger.add_start_step(method='clear_cart')
            try:
                remove_button = self.find_element_by_text('Удалить выбранные')
                remove_button.click()
                self.click_accept_button_yes()
                self.assert_word(self.get_empty_cart_locator, 'Сейчас в корзине нет товаров')
                print('Корзина очищена')
            except selenium.common.exceptions.TimeoutException:
                print('Корзина пустая, товары не были добавлены')
            Logger.add_end_step(url=self.driver.current_url, method='clear_cart')
