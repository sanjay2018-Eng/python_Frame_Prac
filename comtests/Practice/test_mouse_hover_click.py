from pages.frames.framePage import frame_Page_fields
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods
import pytest_check as check
import pytest


class Test_validate_mouse_hover(BaseClass):

    @pytest.mark.skip
    def test_mousehover_click(self):
        log = self.getLogger()
        log.info("\n*** Test Case - test_mousehover_click ***\n")
        res = CustomMethods(self.driver)
        framePage = frame_Page_fields(self.driver)
        res.mouse_hover_element(framePage.mousehoverBtn_locator, framePage.mousehoverBtn_locatortype)
        ele = res.wait_visiblity_element(framePage.hover_menu_locator, framePage.hover_menu_locatortype)
        check.is_not_none(ele)
        res.mouse_hover_click(framePage.hover_topmenu_locator, framePage.hover_topmenu_locatortype)