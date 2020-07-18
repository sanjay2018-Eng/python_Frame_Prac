from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class CustomMethods():
    log = BaseClass().getLogger()

    def __init__(self, driver):
        self.driver = driver

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
            CustomMethods.info("Element not present")
        return element

    def sendKeysElement(self, data, locator, locatorType):
        try:
            self.waitForElement(locator, locatorType, 10)
            ele = self.getElement(locator, locatorType)
            ele.send_keys(data)
        except:
            CustomMethods.log.info("Data not entered")


    def waitForElement(self, locator, locatorType, timeout=20, pollFrequency=0.5):
        bytype = None
        try:
            CustomMethods.log.info("Waiting for element with  locator "+str(locator)+" "+str(locatorType))
            bytype = self.getBytype(locatorType)
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                ElementNotVisibleException, ElementNotSelectableException])
            wait.until(expected_conditions.presence_of_element_located((bytype, locator)))
        except:
            CustomMethods.log.error("Element not found --> "+str(bytype)+str(locator))

    def clickElement(self, locator, locatorType):
        try:
            self.waitForElement(locator, locatorType)
            element = self.getElement(locator, locatorType)
            element.click()
        except:
            CustomMethods.log("Element not clicked with Locator --> "+str(locator)+" Locator type --> "+str(locatorType))

    def isAlertPresent(self):
        try:
            wait = WebDriverWait(self.driver,timeout=10, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])
            wait.until(expected_conditions.alert_is_present())
            CustomMethods.log.info("Alert is present")
            return True
        except:
            CustomMethods.log.error("Alert not present")
            return False

    def switch_altert_Accept(self):
        try:
            al = self.driver.switch_to.alert
            al.accept()
            CustomMethods.log.info("clicked on accept in alert")
        except:
            CustomMethods.log.error("Did not click on accept in alert ")

    def switch_alert_dismiss(self):
        try:
            al = self.driver.switch_to.alert
            al.dismiss()
            CustomMethods.log.info("Clicked on dismiss in alert")
        except:
            CustomMethods.log.error("did not click on dismiss in alert")
