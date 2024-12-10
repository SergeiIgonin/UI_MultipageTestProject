import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language')


@pytest.fixture(scope="function", autouse=True)    # "scope=function" будет создавать объект драйвера для каждого теста
def driver(request):
    user_language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    # options.add_argument('--no-sandbox')
    options.add_argument('-start-maximized')
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver                   # данная конструкция создает объект драйвера внутри тестовых классов
    yield driver
    driver.quit()
