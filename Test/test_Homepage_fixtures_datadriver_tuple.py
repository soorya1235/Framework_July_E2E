import pytest

from Pageobjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class Testhomepage(BaseClass):

    def test_loginpage(self,passdata):
        hp = HomePage(self.driver)
        name = hp.getname()
        name.send_keys(passdata[0])
        email = hp.getemail()
        email.send_keys(passdata[1])
        epass = hp.getpass()
        epass.send_keys(passdata[2])
        sel = hp.getdrop()
        d = Select(sel)
        d.select_by_index(1)
        ds = hp.getdate()
        ds.send_keys("02-03-1983")
        sb= hp.getsubmit()
        sb.click()
        fullmessage = hp.getmessage().text
        self.driver.refresh()

@pytest.fixture(params=[("soorya","abcd@134@gmail.com","govinda"),("shekar","abcd@134@gmail.com","dunder")])
def passdata(request):
    return request.param
