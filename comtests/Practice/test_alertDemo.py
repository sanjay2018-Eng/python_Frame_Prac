import pytest

from pages.home.login_page import HomePage
from utilities.BaseClass import BaseClass
import pytest_check as check

from utilities.reusablemethods import CustomMethods


class TestAlert(BaseClass):

    @pytest.mark.skip
    def test_alert_ok(self):
        log = self.getLogger()
        res = CustomMethods(self.driver)
        log.info("\n*** Executing test case for alert only with OK button *** \n")
        hpage = HomePage(self.driver)
        hpage.enterDataInAlertBox("only accept")
        hpage.click_alert_btn()
        check.is_true(res.isAlertPresent())
        res.switch_altert_Accept()
        check.is_false(res.isAlertPresent())

    @pytest.mark.skip
    def test_alert_dismiss(self):
        log = self.getLogger()
        res = CustomMethods(self.driver)
        log.info("\n*** Executing test case for alert with both Ok and dismiss ***\n")
        hpage = HomePage(self.driver)
        hpage.enterDataInAlertBox("Both dismiss and Ok")
        hpage.click_confirm_Btn()
        check.is_true(res.isAlertPresent())
        res.switch_alert_dismiss()
        check.is_false(res.isAlertPresent())