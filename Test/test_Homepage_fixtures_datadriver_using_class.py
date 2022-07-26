import pytest
import allure
from allure_commons.types import AttachmentType

from Pageobjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class Testhomepage(BaseClass):

    def test_loginpage(self,passdata):
        logger = self.getLogger()
        hp = HomePage(self.driver)
        name = hp.getname()
        name.send_keys(passdata['firstname'])
        logger.info("Entering the firstname"+passdata['firstname'])
        email = hp.getemail()
        email.send_keys(passdata['email'])
        logger.info("Entering the email" + passdata['email'])
        epass = hp.getpass()
        epass.send_keys(passdata['lastname'])
        logger.info("Entering the password" + passdata['lastname'])
        sel = hp.getdrop()
        d = Select(sel)
        #d.select_by_visible_text(passdata["gender"])
        #logger.info("Entering the Gender" + passdata['gender'])
        #cd.select_by_index(2)
        ds = hp.getdate()
        ds.send_keys("02-03-1983")
        sb= hp.getsubmit()
        sb.click()
        fullmessage = hp.getmessage().text
        logger.info(fullmessage)
        assert "oneSuccess!" in fullmessage

        allure.attach(self.driver.get_screenshot_as_png(),name="TestLogin",
                      attachment_type=AttachmentType.PNG)
        self.driver.refresh()

#Note,Here we reading from excel data to pass the data.
#Note,we can alos just call the variable,instead like HomePageData.home_page_data,instead of calling
#getTestData Function

@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
def passdata(request):
    return request.param
