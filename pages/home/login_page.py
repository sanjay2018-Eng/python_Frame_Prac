from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.res = CustomMethods(self.driver)
        self.log = BaseClass().getLogger()



    #**** Locators ****
    alert_txt_box_locator = "name"
    alert_box_loctype = "ID"



    def enterDataInAlertBox(self, data):
        self.log.info("Entering the text in alert text Box")
        self.res.sendKeysElement(data, self.alert_txt_box_locator, self.alert_box_loctype)


