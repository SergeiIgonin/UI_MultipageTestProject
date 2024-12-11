import pytest
from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption('--language')
#
#
# @pytest.fixture(scope="function", autouse=True)    # "scope=function" будет создавать объект драйвера для каждого теста
# def driver(request):
#     user_language = request.config.getoption("language")
#     options = webdriver.ChromeOptions()
#     # options.add_argument('--headless=new')
#     # options.add_argument('--no-sandbox')
#     options.add_argument('-start-maximized')
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#     driver = webdriver.Chrome(options=options)
#     request.cls.driver = driver                   # данная конструкция создает объект драйвера внутри тестовых классов
#     yield driver
#     driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Select browser language")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver= None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # options.add_argument('--headless=new')
        # options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        print(f"\nstart chrome browser with language '{user_language}' for test...")
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        # options.set_headless()
        driver = webdriver.Firefox(options=options)
        print(f"\nstart firefox browser with language '{user_language}' for test...")
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    yield driver
    print("\nquit browser..")
    driver.quit()
