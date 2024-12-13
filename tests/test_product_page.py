import pytest, allure
from base.base_test import BaseTest
from config.links import Links
offers = Links.offers


@allure.feature("Product page Functionality for guest")
@pytest.mark.like_guest
class TestGuestAddToCartFromProductPage(BaseTest):
    @allure.title('Проверка отсутствия для гостя на странице товара сообщения об успехе до того, как товар добавлен в корзину')
    @allure.severity("Major")
    def test_guest_cant_see_success_message_before_adding_product_to_cart(self):
        self.product_page.open()
        self.product_page.should_not_be_success_message()
        self.product_page.make_screenshot("Success")

    @allure.title('Проверка появления для гостя на странице товара сообщение об успехе после добавления товара в корзину')
    @allure.severity("Minor")
    @pytest.mark.xfail(reason="Тест упал, т.к. был success_message")
    def test_guest_should_see_success_message_after_adding_product_to_cart(self):
        self.product_page.open()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_not_be_success_message()     # Пример падающего теста: здесь нужен метод "should_be_success_message"

    @allure.title('Проверка исчезновения со страницы товара сообщения об успехе (пример некорректной проверки)')
    @allure.severity("Trivial")
    @pytest.mark.xfail(reason="Тест упал, т.к. на стр. ничего не исчезло")
    def test_message_disappeared_after_adding_product_to_cart(self):
        self.product_page.open()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_see_element_disappear()  # Пример падающего теста: метод лишний, т.к. SUCCESS_MESSAGE не должен исчезать

    @allure.title('Проверка наличия для гостя на странице товара ссылки для перехода на страницу логина')
    @allure.severity("Major")
    def test_guest_should_see_login_link_on_product_page(self):
        self.product_page.open()
        self.product_page.should_be_login_link()
        self.product_page.make_screenshot("Success")

    @allure.title('Проверка доступности для гостя перехода со страницы товара на страницу логина')
    @allure.severity("Major")
    @pytest.mark.smoke
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.product_page.open()
        self.product_page.go_to_login_page()
        self.product_page.make_screenshot("Success")

    @allure.title('Параметризованная проверка возможности гостю добавить товар в корзину')
    @allure.severity("Critical")
    @pytest.mark.parametrize('offer', offers)
    def test_guest_can_add_product_to_cart(self, offer):
        self.product_page.open_with_params(offer)
        self.product_page.should_be_button_add_to_cart()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_be_correct_product_name()
        self.product_page.should_be_correct_product_price()
        self.product_page.make_screenshot("Success")

    @allure.title('Проверка изначально пустой корзины при переходе в нее со страницы товара в режиме гостя')
    @allure.severity("Major")
    @pytest.mark.smoke
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self):
        self.product_page.open()
        self.product_page.go_to_cart()
        self.cart_page.present_text_about_empty_cart()
        self.cart_page.is_cart_empty()
        self.cart_page.make_screenshot("Success")


@allure.feature("Product page Functionality for user")
@pytest.mark.like_user
class TestUserAddToCartFromProductPage(BaseTest):
    @allure.title('Проверка возможности пользователю добавить товар в корзину')
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_user_can_add_product_to_cart(self):
        self.login_page.open()
        self.login_page.register_new_user(self.data.EMAIL, self.data.PASSWORD)
        self.login_page.should_be_authorized_user()
        self.product_page.open()
        self.product_page.should_be_button_add_to_cart()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_be_correct_product_name()
        self.product_page.should_be_correct_product_price()
        self.product_page.make_screenshot("Success")

    @allure.title('Проверка отсутствия для пользователя на странице товара сообщения об успехе до того, как товар добавлен в корзину')
    @allure.severity("Major")
    def test_user_cant_see_success_message_before_adding_product_to_cart(self):
        self.login_page.open()
        self.login_page.login_user(self.data.EMAIL, self.data.PASSWORD)
        self.login_page.should_be_authorized_user()
        self.product_page.open()
        self.product_page.should_not_be_success_message()
        self.product_page.make_screenshot("Success")

    @allure.title('Проверка появления для пользователя на странице товара сообщение об успехе после добавления товара в корзину')
    @allure.severity("Minor")
    def test_user_should_see_success_message_after_adding_product_to_cart(self):    # разобраться в падении тест
        self.login_page.open()
        self.login_page.login_user(self.data.EMAIL, self.data.PASSWORD)
        self.login_page.should_be_authorized_user()
        self.product_page.open()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_be_success_message()
