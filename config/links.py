import pytest


class Links:

    MAIN_PAGE = "http://selenium1py.pythonanywhere.com"

    LOGIN_PAGE = f"{MAIN_PAGE}/accounts/login/"
    CART_PAGE = f"{MAIN_PAGE}/basket/"
    PRODUCT_PAGE = f"{MAIN_PAGE}/catalogue/coders-at-work_207/?promo=offer"

    'Входные параметры для теста (tests/test_product_page.py::test_guest_can_add_product_to_cart)'
    offers = ["6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]
