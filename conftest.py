import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Select browser language")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        print(f"\nstart chrome browser with language '{user_language}' for test...")
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        print(f"\nstart firefox browser with language '{user_language}' for test...")
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    yield driver
    print("\nquit browser..")
    driver.quit()
