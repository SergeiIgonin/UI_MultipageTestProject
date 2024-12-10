class Links:

    MAIN_PAGE = "http://selenium1py.pythonanywhere.com"

    LOGIN_PAGE = f"{MAIN_PAGE}/accounts/login/"
    CART_PAGE = f"{MAIN_PAGE}/basket/"
    PRODUCT_PAGE = f"{MAIN_PAGE}/catalogue/coders-at-work_207/?promo=offer"

    # params = ["6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]
    # @pytest.mark.parametrize('param', params)
    # def test_guest_can_add_product_to_cart(driver, param):
    #     url = f"{PRODUCT_PAGE}{param}"
    #     product_page = ProductPage(driver, url)
    #     product_page.open()
    #     product_page.should_be_button_add_to_cart()
    #     product_page.add_product_to_cart()
    #     product_page.solve_quiz_and_get_code()
    #     product_page.should_be_correct_product_name()
    #     product_page.should_be_correct_product_price()
