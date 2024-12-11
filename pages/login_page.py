import allure, time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    REGISTER_FORM = ("xpath", "//form[@id='register_form']")
    REG_EMAIL_FIELD = ("xpath", "//input[@id='id_registration-email']")
    REG_PASSWORD_FIELD1 = ("xpath", "//input[@id='id_registration-password1']")
    REG_PASSWORD_FIELD2 = ("xpath", "//input[@id='id_registration-password2']")
    REG_SUBMIT_BUTTON = ("xpath", "//button[@value='Register']")

    LOGIN_FORM = ("xpath", "//form[@id='login_form']")
    LOGIN_EMAIL_FIELD = ("xpath", "//input[@id='id_login-username']")
    LOGIN_PASSWORD_FIELD = ("xpath", "//input[@id='id_login-password']")
    LOGIN_SUBMIT_BUTTON = ("xpath", "//button[@name='login_submit']")

    'Проверка того, что открыта именно страница регистрации/авторизации'
    def should_be_login_url(self):
        assert "pythonanywhere" in self.driver.current_url, "Ошибка в URL"

    'Проверка наличия формы авторизации'
    def should_be_login_form(self):
        assert self.is_element_present(*self.LOGIN_FORM), "Отсутствует форма логина"

    'Проверка наличия формы регистрации'
    def should_be_register_form(self):
        assert self.is_element_present(*self.REGISTER_FORM), "Отсутствует форма регистрации"

    'Регистрация нового пользователя (привинтить к шагам with allure step.."Enter login","Enter password","Click submit button")'
    def register_new_user(self, email, password):  # метод принимает на вход email и password, которые мы передадим в тесте, в методе setup
        self.wait.until(EC.element_to_be_clickable(self.REG_EMAIL_FIELD)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.REG_PASSWORD_FIELD1)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.REG_PASSWORD_FIELD2)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.REG_SUBMIT_BUTTON)).click()

    'Авторизация пользователя'
    def login_user(self, email, password):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_EMAIL_FIELD)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_SUBMIT_BUTTON)).click()
