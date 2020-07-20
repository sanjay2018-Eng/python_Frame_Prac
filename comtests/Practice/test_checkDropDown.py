import pytest
import pytest_check as check

from pages.home.login_page import HomePage
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods


class Test_dropdown_validation(BaseClass):

    @pytest.mark.skip
    def test_dropdown_staticDropDown(self):
        log = self.getLogger()
        res = CustomMethods(self.driver)
        hPage = HomePage(self.driver)
        hPage.select_visibleText_In_DropDown("Option2")
        log.info("Selected the option Option 2")
        check.is_true(res.compare_two_strings(hPage.get_selected_option(), "Option2"))

    @pytest.mark.skip
    def test_allValues_In_DropDown(self):
        log = self.getLogger()
        res = CustomMethods(self.driver)
        hPage = HomePage(self.driver)
        count = hPage.print_all_Values_dropdown()
        log.info("checking the count of values in drop down")
        check.is_true(count == 4)

    @pytest.mark.skip
    def test_select_value_from_autosuggestion(self):
        log = self.getLogger()
        res = CustomMethods(self.driver)
        hPage = HomePage(self.driver)
        hPage.select_value_from_autocomplete("aus", "austria")
        text_selected = res.getText_from_textbox(hPage.autocomplete_locator, hPage.autocomplete_locatortype)
        log.info("Auto complete text --> "+text_selected)
        check.is_true(res.compare_two_strings(text_selected, "austria"))
