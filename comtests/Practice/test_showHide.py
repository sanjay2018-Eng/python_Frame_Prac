from pages.frames.framePage import frame_Page_fields
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods
import pytest_check as check
import pytest


class Test_showHide_validation(BaseClass):

    @pytest.mark.skip
    def test_validate_showHideBtn(self):
        log = self.getLogger()
        log.info("\n*** Test Case - test_validate_showHideBtn ***\n")
        res = CustomMethods(self.driver)
        framePage = frame_Page_fields(self.driver)
        eleShow = framePage.clickShowBtn()
        check.is_not_none(eleShow)
        eleHide = framePage.clickHideBtn()
        check.is_none(eleHide)
        ele_sec = framePage.clickShowBtn()
        check.is_not_none(ele_sec)
        framePage.enterTxtInShowhideTxtBox("Entering value")
        actualText = res.getText_from_textbox(framePage.showHideTxtBox_locator, framePage.showHideTxtBox_locatortype)
        log.info("Actual - > "+actualText+" Expected -> Entering value")
        check.is_true(res.compare_two_strings(actualText, "Entering value"))