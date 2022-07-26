import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
driver = None


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    print("This is called before execution => suitesetup")
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("the browsername is {}".format(browser_name))
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        print("the browsername is {}".format(browser_name))
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print("This is called before execution => suiteteardown")
    driver.quit()
