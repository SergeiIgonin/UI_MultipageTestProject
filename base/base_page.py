import allure
from config.links import Links
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from allure_commons.types import AttachmentType              # позволяет добавлять в Allure-reports скриншоты
from selenium.webdriver.chrome.webdriver import WebDriver    # позволяет автоматически подтягивать методы драйвера после ввода "driver."


class BasePage:
    PAGE_URL = None

    GO_TO_CART_BUTTON = ("xpath", "//a[@class='btn btn-default']")
    LOGIN_LINK = ("xpath", "//a[@id='login_link']")
    LOGIN_LINK_INVALID = ("xpath", "//a[@id='kogin_link']")  # пример кривого локатора для демонстрации падающего теста
    USER_ICON = ("xpath", "//i[@class='icon-user']")

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 5, poll_frequency=1)

    def open(self):
        with allure.step(f"Открытие страницы {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    def open_with_params(self, offers):
        with allure.step(f"Открытие страницы {Links.PRODUCT_PAGE}{offers}"):
            self.driver.get(Links.PRODUCT_PAGE + offers)

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Переход на страницу корзины")
    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.GO_TO_CART_BUTTON)).click()

    @allure.step("Переход на страницу логина")
    def go_to_login_page(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()

    @allure.step("Проверка наличия ссылки на страницу логина")
    def should_be_login_link(self):
        assert self.is_element_present(*self.LOGIN_LINK), "Отсутствует ссылка на страницу регистрации/авторизации"

    @allure.step("Проверка факта авторизации пользователя")
    def should_be_authorized_user(self):
        assert self.is_element_present(*self.USER_ICON), "Пользователь не авторизован — отсутствует user icon"

    @allure.step("Проверка присутствия элемента на странице")
    def is_element_present(self, method, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((method, locator)))
        except NoSuchElementException:
            return False
        return True

    @allure.step("Проверка отсутствия элемента на странице (ждем 5 сек.)")
    def is_not_element_present(self, method, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((method, locator)))
        except TimeoutException:
            return True
        return False

    @allure.step("Проверка исчезновения изначально существующего элемента со страницы (ждем 5 сек.)")
    def is_disappeared(self, method, locator):
        try:
            self.wait(TimeoutException).until_not(EC.visibility_of_element_located((method, locator)))
        except TimeoutException:
            return False
        return True
