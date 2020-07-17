from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class CustomMethods():
    def __init__(self, driver):
        self.driver = driver
        self.log = BaseClass().getLogger()

    def getBytype(self, locatorType):
        locatorType = str(locatorType.lower())
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.__name__
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Not valid locator Type")
        return False

    def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = str(locatorType.lower())
            byType = self.getBytype(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            self.log.info("Element not present")
        return element

    def sendKeysElement(self, data, locator, locatorType):
        try:
            ele = self.getElement(locator, locatorType)
            ele.send_keys(data)
        except:
            self.log.info("Data not entered")
