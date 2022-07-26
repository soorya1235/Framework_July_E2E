from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pageobjects.CheckOutPage import CheckOutPage
from Pageobjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from Utilities.Waiterclass import Waiterclass
from selenium.webdriver.support import expected_conditions as EC


class Testone(BaseClass):

    def test_invoke(self):
        hm = HomePage(self.driver)
        cp = hm.gotoshopitems()
        card_items = cp.getcartitems()
        count = -1
        for card in card_items:
            count = count + 1
            print(card.text)
            if(card.text == "Blackberry"):
                print("Matched")
                print(count)
                cp.checkoutcart()[count].click()
                sp = cp.gotoshopping()
                sp.exitshopping()
                sp.enterdata()
                self.verifyLinkPresence(sp.indiachhose)
                sp.clickcheckbox()
                message = sp.getsucesstext().text
                print(message)
                #log.info("Text received from application is " + textMatch)
                assert ("Success! Thank you!" in message)

