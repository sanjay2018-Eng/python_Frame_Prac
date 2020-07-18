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




    def enterDataInAlertBox(self, data):
        HomePage.log.info("Entering the text in alert text Box")
        self.res.sendKeysElement(data, self.alert_txt_box_locator, self.alert_box_loctype)

    def click_alert_btn(self):
        HomePage.log.info("clicking on the alert button")
        self.res.clickElement(self.alertBtn_locator, self.alertBtn_locatorType)

    def click_confirm_Btn(self):
        HomePage.log.info("clicking on the confirm button")
        self.res.clickElement(self.confirmBtn_locator, self.confirBtn_locatorType)

