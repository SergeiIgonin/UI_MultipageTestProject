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
#-------------------------------------
#   dashboard_page
#
#   @allure.step("Click on 'My Info' link")
#   def click_my_info_link(self):
#       self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()
#----------
#   personal_page
#
#   def change_name(self, new_name):
#   with allure.step(f"Change name on '{new_name}'"):
#       first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
#       first_name_field.send_keys(Keys.COMMAND + "A")   # юзаем Keys т.к. эл. перекрывается др.эл. и метод .clear не срабатывает
#       first_name_field.send_keys(Keys.BACKSPACE)
#       first_name_field.send_keys(new_name)
#       self.name = new_name
#
#   @allure.step("Save changes")
#   def save_changes(self):
#       self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
#
#   @allure.step("Changes has been saved successfuly")
#   def is_changes_saved(self):
#       self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
#       self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
#       self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))
