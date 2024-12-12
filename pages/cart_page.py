import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    PAGE_URL = Links.CART_PAGE

    CART_MSG = ("xpath", "//div[@id='content_inner']/p")
    PRODUCT_AVAILABILITY_MSG = ("xpath", "//h2[@class='col-sm-6 h3']")
    QUANTITY_OF_GOODS_FIELD = ("xpath", "//div/input[@id='id_form-0-quantity']")

    @allure.step("Проверка того, что корзина пуста")
    def is_cart_empty(self):
        assert self.is_not_element_present(*self.PRODUCT_AVAILABILITY_MSG), "Корзина не пуста, есть текст 'Товары в корзине'"
        assert self.is_not_element_present(*self.QUANTITY_OF_GOODS_FIELD),  "Корзина не пуста, есть поле с количеством товаров"

    @allure.step("Проверка наличия подтверждающего сообщения о пустой корзине")
    def present_text_about_empty_cart(self):
        # cart_message = self.driver.find_element(*self.CART_MSG)
        cart_message = self.wait.until(EC.visibility_of_element_located(self.CART_MSG))
        assert "корзина пуста" or "basket is empty" or "carrito esta vacío" or "panier est vide" in cart_message.text, "Корзина не пуста"
