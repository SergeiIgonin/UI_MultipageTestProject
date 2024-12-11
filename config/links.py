import pytest


class Links:

    MAIN_PAGE = "http://selenium1py.pythonanywhere.com"

    LOGIN_PAGE = f"{MAIN_PAGE}/accounts/login/"
    CART_PAGE = f"{MAIN_PAGE}/basket/"
    PRODUCT_PAGE = f"{MAIN_PAGE}/catalogue/coders-at-work_207/?promo=offer"

    params = ["6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]
