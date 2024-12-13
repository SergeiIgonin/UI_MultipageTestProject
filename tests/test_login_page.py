import pytest, allure
from base.base_test import BaseTest


@allure.feature("Login page Functionality")
class TestLoginPage(BaseTest):
    @allure.title('Проверка наличия на странице логина форм регистрации и авторизации')
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_should_be_login_page(self):
        self.login_page.open()
        self.login_page.should_be_login_url()
        self.login_page.should_be_login_form()
        self.login_page.should_be_register_form()
        self.login_page.make_screenshot("Success")
