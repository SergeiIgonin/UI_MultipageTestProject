import pytest, allure
from base.base_test import BaseTest
from config.links import Links
offers = Links.offers


@pytest.mark.like_guest
class TestGuestAddToCartFromProductPage(BaseTest):

    @pytest.mark.smoke
    def test_guest_can_add_product_to_cart(self):
        self.product_page.open()
        self.product_page.should_be_button_add_to_cart()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_be_correct_product_name()
        self.product_page.should_be_correct_product_price()
        self.product_page.make_screenshot("Success")

    def test_guest_cant_see_success_message_before_adding_product_to_cart(self):
        self.product_page.open()
        self.product_page.should_not_be_success_message()
        self.product_page.make_screenshot("Success")

    @pytest.mark.xfail(reason="Тест упал, т.к. был success_message")
    def test_guest_should_see_success_message_after_adding_product_to_cart(self):
        self.product_page.open()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_not_be_success_message()   # Пример падающего теста: здесь нужен был метод "should_be_success_message"

    @pytest.mark.xfail(reason="Тест упал, т.к. на стр. ничего не исчезло")
    def test_message_disappeared_after_adding_product_to_cart(self):
        self.product_page.open()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_see_element_disappear()    # Пример падающего теста: метод лишний, SUCCESS_MESSAGE не должен исчезать

    def test_guest_should_see_login_link_on_product_page(self):
        self.product_page.open()
        self.product_page.should_be_login_link()
        self.product_page.make_screenshot("Success")

    @pytest.mark.smoke
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.product_page.open()
        self.product_page.go_to_login_page()
        self.product_page.make_screenshot("Success")

    @pytest.mark.parametrize('offer', offers)
    def test_guest_can_add_product_to_cart(self, offer):
        self.product_page.open_with_params(offer)
        self.product_page.should_be_button_add_to_cart()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_be_correct_product_name()
        self.product_page.should_be_correct_product_price()
        self.product_page.make_screenshot("Success")

    @pytest.mark.smoke
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self):
        self.product_page.open()
        self.product_page.go_to_cart()
        self.cart_page.present_text_about_empty_cart()
        self.cart_page.is_cart_empty()
        self.cart_page.make_screenshot("Success")


@pytest.mark.like_user
class TestUserAddToCartFromProductPage(BaseTest):
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

    def test_user_cant_see_success_message_before_adding_product_to_cart(self):
        self.login_page.open()
        self.login_page.login_user(self.data.EMAIL, self.data.PASSWORD)
        self.login_page.should_be_authorized_user()
        self.product_page.open()
        self.product_page.should_not_be_success_message()
        self.product_page.make_screenshot("Success")
