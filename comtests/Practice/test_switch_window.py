import pytest
from pages.home.login_page import HomePage
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods
import pytest_check as check

class Test_Window_switch(BaseClass):

    @pytest.mark.skip
    def test_switchWindow_validateURL(self):
        log = self.getLogger()
        log.info("\n*** Test Case - test_switchWindow_validateURL ***\n")
        res = CustomMethods(self.driver)
        hPage = HomePage(self.driver)
        hPage.clickOpewindowBtn()
        res.switchToChildWindow()
        current_url = res.getcurrentURL()
        check.equal(current_url, "http://www.qaclickacademy.com/")
        res.switchToParentWindow()
        parentUrl = res.getcurrentURL()
        check.equal(parentUrl, "https://www.rahulshettyacademy.com/AutomationPractice/")
        log.info("second check Parent url is --> "+parentUrl)
