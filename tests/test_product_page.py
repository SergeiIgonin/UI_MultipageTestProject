import pytest, time, allure, faker
from base.base_test import BaseTest
from config.links import Links
from pages import product_page


#
#
@pytest.mark.like_user
class TestGuestAddToCartFromProductPage(BaseTest):
#
#     def test_guest_can_add_product_to_cart(self):
#         self.product_page.open()
#         time.sleep(1)
#         self.product_page.should_be_button_add_to_cart()
#         self.product_page.add_product_to_cart()
#         self.product_page.solve_quiz_and_get_code()
#         self.product_page.should_be_correct_product_name()
#         self.product_page.should_be_correct_product_price()
#
#     def test_guest_cant_see_success_message_before_adding_product_to_cart(self):
#         self.product_page.open()
#         self.product_page.should_not_be_success_message()
#
#     @pytest.mark.xfail(reason="Пример падающего теста, т.к. success_message присутствует")
#     def test_guest_should_see_success_message_after_adding_product_to_cart(self):
#         self.product_page.open()
#         self.product_page.add_product_to_cart()
#         self.product_page.solve_quiz_and_get_code()
#         self.product_page.should_not_be_success_message()
#
#     @pytest.mark.xfail(reason="Пример падающего теста, т.к. в данном случае на странице ничего не исчезает")
#     def test_message_disappeared_after_adding_product_to_cart(self):
#         self.product_page.open()
#         self.product_page.add_product_to_cart()
#         self.product_page.solve_quiz_and_get_code()
#         self.product_page.should_see_element_disappear()
#
#     def test_guest_should_see_login_link_on_product_page(self):
#         self.product_page.open()
#         self.product_page.should_be_login_link()
#
#     def test_guest_can_go_to_login_page_from_product_page(self):
#         self.product_page.open()
#         self.product_page.go_to_login_page()
#         time.sleep(1)

    # params = ["6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]

    params = Links.params

    @pytest.mark.parametrize('param', params)
    def test_guest_can_add_product_to_cart(self, param):
        self.product_page.open_with_params(param)
        time.sleep(1)
        self.product_page.should_be_button_add_to_cart()
        self.product_page.add_product_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_be_correct_product_name()
        self.product_page.should_be_correct_product_price()

    # @pytest.mark.smoke
    # def test_guest_cant_see_product_in_cart_opened_from_product_page(self):
    #     self.product_page.open()
    #     time.sleep(1)
    #     self.product_page.go_to_cart()
    #     time.sleep(1)
    #     self.cart_page.present_text_about_empty_cart()
    #     self.cart_page.is_cart_empty()
# pytest -v D:\PycharmProjects\UI_MultipageTestProject\tests\test_product_page.py
#
# @pytest.mark.like_user
# class TestUserAddToCartFromProductPage(BaseTest):
#
#     @pytest.mark.smoke
#     def test_user_can_add_product_to_cart(self):
#         self.login_page.open()
#         self.login_page.register_new_user(self.data.EMAIL, self.data.PASSWORD)
#         self.login_page.should_be_authorized_user()
#         self.product_page.open()
#         self.product_page.should_be_button_add_to_cart()
#         self.product_page.add_product_to_cart()
#         self.product_page.solve_quiz_and_get_code()
#         self.product_page.should_be_correct_product_name()
#         self.product_page.should_be_correct_product_price()
#
#     @pytest.mark.smoke
#     def test_user_cant_see_success_message_before_adding_product_to_cart(self):
#         self.login_page.open()
#         self.login_page.login_user(self.data.EMAIL, self.data.PASSWORD)
#         time.sleep(1)
#         self.login_page.should_be_authorized_user()
#         self.product_page.open()
#         time.sleep(1)
#         self.product_page.should_not_be_success_message()
