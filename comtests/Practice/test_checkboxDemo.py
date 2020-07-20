from pages.home.login_page import HomePage
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods
import pytest_check as check

class Test_checkbox(BaseClass):

    def test_validate_checkbox_selection(self):
        log = self.getLogger()
        log.info("\n*** Test Case - validate_checkbox_selection ***\n")
        res = CustomMethods(self.driver)
        hPage = HomePage(self.driver)
        hPage.check_chBox(["option1", "option3"])
        result = res.validate_ch_radio_is_selected(["option1", "option3"], hPage.chkBoxList_locator, hPage.chkBoxList_locatortype)
        check.is_true(result)

    def test_validate_radioBtn_selection(self):
        log = self.getLogger()
        log.info("\n*** Test Case - validate_radioBtn_selection ***\n")
        res = CustomMethods(self.driver)
        hPage = HomePage(self.driver)
        hPage.check_radioBtn(["radio1", "radio2"])
        result = res.validate_ch_radio_is_selected(["radio2"], hPage.radioList_locator, hPage.radioList_locatortype)
        check.is_true(result)
