import pytest, allure
from base.base_test import BaseTest


@pytest.mark.login_guest
class TestLoginFromMainPage(BaseTest):
    @allure.title('Проверка наличия для гостя ссылки для регистрации/авторизации')
    def test_guest_should_see_login_link_on_main_page(self):
        self.main_page.open()
        self.main_page.should_be_login_link()
        self.main_page.make_screenshot("Success")

    @allure.title('Проверка возможности перехода гостя с главной страницы на страницу регистрации/авторизации')
    @pytest.mark.smoke
    def test_guest_can_go_to_login_page_from_login_page(self):
        self.main_page.open()
        self.main_page.go_to_login_page()
        self.login_page.should_be_login_url()
        self.login_page.make_screenshot("Success")

    @allure.title('Проверка того, что корзина изначально будет пуста для гостя при переходе в нее с главной страницы')
    def test_guest_cant_see_product_in_cart_opened_from_main_page(self):
        self.main_page.open()
        self.main_page.go_to_cart()
        self.cart_page.present_text_about_empty_cart()
        self.cart_page.is_cart_empty()
        self.cart_page.make_screenshot("Success")
