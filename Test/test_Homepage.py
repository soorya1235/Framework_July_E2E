from Pageobjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class Testhomepage(BaseClass):

    def test_loginpage(self):
        hp = HomePage(self.driver)
        name = hp.getname()
        name.send_keys("soorya")
        email = hp.getemail()
        email.send_keys("sarvan135@yahoo.com")
        epass = hp.getpass()
        epass.send_keys("soorya")
        sel = hp.getdrop()
        d = Select(sel)
        d.select_by_index(1)
        ds = hp.getdate()
        ds.send_keys("02-03-1983")
        sb= hp.getsubmit()
        sb.click()
        fullmessage = hp.getmessage().text


