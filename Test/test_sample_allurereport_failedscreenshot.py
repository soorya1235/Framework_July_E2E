import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        print("controal coming inside")
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


def test_setup_function():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://facebook.com")
    driver.maximize_window()

@pytest.mark.usefixtures("log_on_failure")
def test_login():
    #driver.get("http://facebook.com")
    assert 1==2

def test_teardown_function():
    driver.quit()

