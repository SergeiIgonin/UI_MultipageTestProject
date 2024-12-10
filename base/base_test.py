import pytest
from config.data import Data
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class BaseTest:

    data: Data

    cart_page: CartPage
    login_page: LoginPage
    main_page: MainPage
    product_page: ProductPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.cart_page = CartPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.product_page = ProductPage(driver)
