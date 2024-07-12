import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:
    # base locators
    CART_BUTTON = (By.XPATH, "//span[@id='topbox_cart_qty']")
    PROFILE_BUTTON = (By.XPATH, "header__main-link header__main-link-lk hovered-link']")

    def __init__(self, driver):
        self.locator = None
        self.driver = driver

    # getters
    @property
    def get_cart_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CART_BUTTON))

    @property
    def get_profile_button_locator(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PROFILE_BUTTON))

    # actions
    def click_cart_button(self):
        self.get_cart_button_locator.click()
        print('Нажатие кнопки корзины')

    def click_profile_button(self):
        self.get_profile_button_locator.click()
        print('Нажатие кнопки корзины')

    # methods
    def find_element_by_text(self, name_text_element):
        """Метод для поиска элемента по тексту, может работать некорректно в случае,
         если на странице несколько элементов с одним названием"""
        self.locator = f"//*[text()='{name_text_element}']"
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.locator)))

    def print_current_url(self):
        """Метод для печати текущего url"""
        get_url = self.driver.current_url
        print("current url:" + get_url)

    def assert_word(self, word, result):
        """Метод для проверки ключевого слова после перехода страницы"""
        value_word = word.text
        assert value_word == result
        print("Переход на страницу совершен")

    def save_screenshot(self):
        """Метод для создания скришотов"""
        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(f'screenshots/{name_screenshot}')

    def assert_url(self, url_result):
        """Метод для проверки url"""
        url = self.driver.current_url
        assert url == url_result
        print('url проверен')

    def element_hover(self, locator):
        """Наведение на элемент"""
        ActionChains(self.driver).move_to_element(locator).perform()

    def get_texts_from_elements(self, elements):
        """Метод возвращает список текстов атрибутов"""
        k = [x.text for x in elements]
        return k
