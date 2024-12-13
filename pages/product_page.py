import math, allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    PAGE_URL = Links.PRODUCT_PAGE

    ADD_TO_CART_BUTTON = ("xpath", "//button[contains(@class, 'add-to-basket')]")
    SUCCESS_MESSAGE = ("xpath", "(//div[contains(@class, 'alertinner')])[1]")
    PRODUCT_NAME_MSG = ("xpath", "(//div/strong)[3]")
    PRODUCT_NAME_REAL = ("xpath", "//div/h1")
    PRODUCT_PRICE_MSG = ("xpath", "(//div/p/strong)[2]")
    PRODUCT_PRICE_REAL = ("xpath", "//div/p[@class='price_color']")

    @allure.step("Присутствует кнопка 'добавить в корзину'")
    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*self.ADD_TO_CART_BUTTON), "Отсутствует кнопка добавления в корзину"

    @allure.step("Добавление товара в корзину")
    def add_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

    @allure.step("Решение задачи из алерта")
    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    @allure.step("Сообщение об успехе отсутствует")
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), "Есть сообщение об успехе, которого не должно быть"

    @allure.step("Отображается сообщение об успехе")
    def should_be_success_message(self):
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "Отсутствует сообщение об успехе, которое должно быть"

    @allure.step("Сообщение об успехе исчезает со временем")
    def should_see_element_disappear(self):
        assert self.is_element_disappeared(*self.SUCCESS_MESSAGE), "Элемент не исчезает, хотя должен исчезнуть"

    @allure.step("Имя товара из сообщения совпадает с реальным именем товара")
    def should_be_correct_product_name(self):
        product_name_msg = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_MSG))
        product_name_real = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_REAL))
        assert product_name_msg.text == product_name_real.text, "Название товара из сообщения не совпадает с реальным названием товара"

    @allure.step("Цена товара из сообщения совпадает с реальной ценой товара")
    def should_be_correct_product_price(self):
        product_price_msg = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE_MSG))
        product_price_real = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE_REAL))
        assert product_price_msg.text == product_price_real.text, "Стоимость товара из сообщения не совпадает с его реальной стоимостью"
