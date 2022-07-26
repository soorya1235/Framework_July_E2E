import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities.BaseClass import BaseClass

#install allure cmd line,allure pytest,pytest again under the python interpreter,else it will not work.



class Testallure(BaseClass):

    def test_one(self):
        print("one")
        allure.attach(self.driver.get_screenshot_as_png(),name="one",attachment_type=AttachmentType.PNG)

    def test_two(self):
        print("two")
        allure.attach(self.driver.get_screenshot_as_png(), name="two", attachment_type=AttachmentType.PNG)

    def test_three(self):
        print("three")
        allure.attach(self.driver.get_screenshot_as_png(), name="three", attachment_type=AttachmentType.PNG)

    def test_four(self):
        print("four")
        allure.attach(self.driver.get_screenshot_as_png(), name="four", attachment_type=AttachmentType.PNG)

    def test_five(self):
        print("five")
        allure.attach(self.driver.get_screenshot_as_png(), name="five", attachment_type=AttachmentType.PNG)

    def test_six(self):
        print("six")
        allure.attach(self.driver.get_screenshot_as_png(), name="six", attachment_type=AttachmentType.PNG)

    def test_seven(self):
        print("seven")
        allure.attach(self.driver.get_screenshot_as_png(), name="seven", attachment_type=AttachmentType.PNG)

