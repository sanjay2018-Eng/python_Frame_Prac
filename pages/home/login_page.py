from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods


class HomePage():
    log = BaseClass().getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.res = CustomMethods(self.driver)

  #**** Locators ****
    alert_txt_box_locator = "name"
    alert_box_loctype = "ID"

    alertBtn_locator = "input[value='Alert']"
    alertBtn_locatorType = "css"

    confirmBtn_locator = "//input[@id='confirmbtn']"
    confirBtn_locatorType = "xpath"

    dropDown_locator = "dropdown-class-example"
    dropDown_locatorType = "ID"

    suggestiveDP_loator = "li[class='ui-menu-item'] div"
    suggestiveDP_locatortype = "css"

    autocomplete_locator = "autocomplete"
    autocomplete_locatortype = "id"

    chkBoxList_locator = "div[id='checkbox-example'] input[type='checkbox']"
    chkBoxList_locatortype = "css"

    radioList_locator = "div[id='radio-btn-example'] input[name='radioButton']"
    radioList_locatortype = "css"

    def enterDataInAlertBox(self, data):
        HomePage.log.info("Entering the text in alert text Box")
        self.res.sendKeysElement(data, self.alert_txt_box_locator, self.alert_box_loctype)

    def click_alert_btn(self):
        HomePage.log.info("clicking on the alert button")
        self.res.clickElement(self.alertBtn_locator, self.alertBtn_locatorType)

    def click_confirm_Btn(self):
        HomePage.log.info("clicking on the confirm button")
        self.res.clickElement(self.confirmBtn_locator, self.confirBtn_locatorType)

    def select_visibleText_In_DropDown(self, option_to_select):
        HomePage.log.info("Selecting the value --> "+option_to_select+" from dropdown")
        self.res.select_visible_text_from_dropdown(option_to_select, self.dropDown_locator, self.dropDown_locatorType)

    def print_all_Values_dropdown(self):
        HomePage.log.info("Printing all values in drop down")
        dp_list = self.res.select_getAllValues_dropdown(self.dropDown_locator, self.dropDown_locatorType)
        for i in dp_list:
            HomePage.log.info(i.text)
        return len(dp_list)

    def get_selected_option(self):
        HomePage.log.info("Get selected option in dropdown")
        sel_value = self.res.get_selected_option_in_dropdown(self.dropDown_locator, self.dropDown_locatorType)
        return sel_value

    def select_value_from_autocomplete(self, inital, value_to_select):
        HomePage.log.info("Selecting value from autocomplete drop down --> "+value_to_select)
        self.res.sendKeysElement(inital, self.autocomplete_locator, self.autocomplete_locatortype)
        self.res.select_values_from_auto_sggestionDP(value_to_select, self.suggestiveDP_loator, self.suggestiveDP_locatortype)

    def check_chBox(self, list_values):
        HomePage.log.info("Selecting the checkbox")
        self.res.check_chBox_radioBtn(list_values, self.chkBoxList_locator, self.chkBoxList_locatortype)

    def check_radioBtn(self, list_values):
        HomePage.log.info("Selecting the radio button")
        self.res.check_chBox_radioBtn(list_values, self.radioList_locator, self.radioList_locatortype)


