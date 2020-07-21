import pytest
from pages.frames.framePage import frame_Page_fields
from pages.home.login_page import HomePage
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods
import pytest_check as check

class Test_switchFrame(BaseClass):

    @pytest.mark.skip
    def test_validate_frame_switching(self):
        log = self.getLogger()
        log.info("\n*** Test Case - test_validate_frame_switching ***\n")
        res = CustomMethods(self.driver)
        hPage = HomePage(self.driver)
        hPage.switch_to_frame()
        framePage = frame_Page_fields(self.driver)
        ele = res.wait_visiblity_element(framePage.earn_locator, framePage.earn_locatortype)
        log.info(ele.text)
        check.is_not_none(ele)
        res.switch_to_parent_frame()
        openWinele = res.wait_visiblity_element(hPage.openWindow_locator, hPage.openwindow_locatortype)
        check.is_not_none(openWinele)



