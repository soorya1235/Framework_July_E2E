import pytest

from Pageobjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class Testhomepage(BaseClass):

    def test_loginpage(self,passdata):
        hp = HomePage(self.driver)
        name = hp.getname()
        name.send_keys(passdata['firstname'])
        email = hp.getemail()
        email.send_keys(passdata['email'])
        epass = hp.getpass()
        epass.send_keys(passdata['pass'])
        sel = hp.getdrop()
        d = Select(sel)
        d.select_by_visible_text(passdata["gender"])
        ds = hp.getdate()
        ds.send_keys("02-03-1983")
        sb= hp.getsubmit()
        sb.click()
        fullmessage = hp.getmessage().text
        self.driver.refresh()

@pytest.fixture(params=[{"firstname":"soorya","email":"abc.com","pass":"test","gender":"Male"},{"firstname":"ramesh","email":"ramesh.com","pass":"test","gender":"Female"}])
def passdata(request):
    return request.param
