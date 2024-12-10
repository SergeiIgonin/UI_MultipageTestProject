import pytest, allure, time
from base.base_test import BaseTest


class TestLoginPage(BaseTest):
    @pytest.mark.smoke
    def test_should_be_login_page(self):
        self.login_page.open()
        time.sleep(1)
        self.login_page.should_be_login_url()
        self.login_page.should_be_login_form()
        self.login_page.should_be_register_form()

