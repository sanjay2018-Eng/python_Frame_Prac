from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
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
            self.wait_visiblity_element(locator, locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            CustomMethods.log.info("Element not present")
        return element

    def getElements(self, locator, locatortype):
        eleList = None
        try:
            locatortype = str(locatortype.lower())
            bytype = self.getBytype(locatortype)
            self.wait_elemets_list(locator, locatortype)
            eleList = self.driver.find_elements(bytype, locator)
            return eleList
        except:
            CustomMethods.log.info("Elements list not present")


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

    def wait_visiblity_element(self, locator, locatortype, timeout=30, pollFrequency=0.5):
        bytype = None
        element = None
        try:
            CustomMethods.log.info("Waiting for visibility of element with  locator -> "+str(locator)+" "+str(locatortype))
            bytype = self.getBytype(locatortype)
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                                ElementNotVisibleException,ElementNotSelectableException])
            element = wait.until(expected_conditions.visibility_of_element_located((bytype, locator)))
            return element
        except:
            CustomMethods.log.error("Element with locator - "+str(locator)+" "+str(locatortype)+"not found")

    def wait_elemets_list(self, locator, locatortype, timeout=30, pollFrequency=0.5):
        bytype = None
        elelist = None
        try:
            bytype = self.getBytype(locatortype)
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            elelist = wait.until(expected_conditions.visibility_of_all_elements_located((bytype, locator)))
            CustomMethods.log.info("Count of elements displayed --> "+str(len(elelist)))
            return elelist
        except:
            CustomMethods.log.error("List not found")

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

    def select_visible_text_from_dropdown(self, option_to_select, locator, locatortype):
        try:
            element = self.getElement(locator, locatortype)
            sel = Select(element)
            sel.select_by_visible_text(option_to_select)
        except:
            CustomMethods.log.info("In except block of select visible text value not selected")

    def select_getAllValues_dropdown(self, locator, locatortype):
        try:
            element = self.getElement(locator, locatortype)
            sel = Select(element)
            all_options_list = sel.options
            return all_options_list
        except:
            CustomMethods.log.error("In except block, all options not returned")

    def get_selected_option_in_dropdown(self, locator, locatortype):
        try:
            element = self.getElement(locator, locatortype)
            sel = Select(element)
            sel_value = sel.first_selected_option
            CustomMethods.log.info("The selected value is --> "+str(sel_value.text))
            return sel_value.text
        except:
            CustomMethods.log.info("In except block of selected option in dropdown. Value not sent")

    def compare_two_strings(self, actual, expected):
        try:
            CustomMethods.log.info("compare actual and expected")
            CustomMethods.log.info("Actual --> "+actual+", Expected --> "+expected)
            if actual.lower() == expected.lower():
                return True
            else:
                CustomMethods.log.warning("Strings dont match -> Actual --> " + actual + ", Expected --> " + expected)
                return False
        except:
            CustomMethods.log.info("In except block of Compare two strings")

    def select_values_from_auto_sggestionDP(self, value_to_select, locator, locatortype):
        try:
            CustomMethods.log.info("Selecting the value --> "+value_to_select+" from auto suggestion")
            eleList = self.getElements(locator, locatortype)
            found = False
            for i in eleList:
                if i.text.lower() == value_to_select.lower():
                    i.click()
                    found = True
                    break
            if found == False:
                CustomMethods.log.info("the value --> "+value_to_select+" not found in drop down ")
        except:
            CustomMethods.log.error("In except block of auto suggestion")
            CustomMethods.log.info("The value not found --> "+value_to_select)

    def getText_from_textbox(self, locator, locatortype):
        try:
            CustomMethods.log.info("Get the text from text box")
            element = self.getElement(locator, locatortype)
            return element.get_attribute("value")
        except:
            CustomMethods.log.info("In except block text not present")

    def check_chBox_radioBtn(self, vlist, locator, locatortype):
        try:
            CustomMethods.log.info("Getting element with locator --> "+str(locator)+" -> "+str(locatortype))
            eleList = self.getElements(locator, locatortype)
            for ele in eleList:
                CustomMethods.log.info("Text of element in list --> "+str(ele.get_attribute("value")))
                text = ele.get_attribute("value")
                for i in vlist:
                    if text == i:
                        if not ele.is_selected():
                            ele.click()
        except Exception as e:
            CustomMethods.log.info("In except block of radio and checkbox")
            CustomMethods.log.info(e)

    def validate_ch_radio_is_selected(self, vlist, locator, locatortype):
        try:
            CustomMethods.log.info("Checking if the checkbox or radio button is selected")
            elelist = self.getElements(locator, locatortype)
            ele_not_selected = []
            for ele in elelist:
                text = ele.get_attribute("value")
                for i in vlist:
                    if text == i:
                        if not ele.is_selected():
                            ele_not_selected.append(text)
            if len(ele_not_selected) == 0:
                CustomMethods.log.info("All checkboxes/Radio Buttons are selected")
                return True
            else:
                CustomMethods.log.error("Following checkbox or radio button are not selected ")
                CustomMethods.log.info(ele_not_selected)
                return False
        except Exception as e:
            CustomMethods.log.info(e)

    def getCurrentWindowHandle(self):
        try:
            parentHandle = self.driver.current_window_handle
            CustomMethods.log.info("CUrrent window handle is --> "+str(parentHandle))
            return parentHandle
        except Exception as e:
            CustomMethods.log.error("Except -> getCurrentWindowHandle -> window not present")

    def switchToChildWindow(self):
        try:
            parentHandle = self.getCurrentWindowHandle()
            allhandles = self.driver.window_handles
            for handle in allhandles:
                if not handle == parentHandle:
                    self.driver.switch_to.window(handle)
                    CustomMethods.log.info("Switched to child window "+str(handle))
                    break
        except:
            CustomMethods.log.info("Except -> switchToChildWindow -> child window not present")

    def getcurrentURL(self):
        try:
            cUrl = self.driver.current_url
            CustomMethods.log.info("Current Url is --> "+str(cUrl))
            return cUrl
        except:
            CustomMethods.log.error("Except block --> getcurrentURL --> Page not present")

    def switchToParentWindow(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
        except:
            CustomMethods.log.error("Except -> switchToParentWindow -> not switched to parent window")


    def switch_to_frame(self, frame_reference):
        try:
            CustomMethods.log.info("switching to frame with reference --> "+frame_reference)
            self.driver.switch_to.frame(frame_reference)
        except Exception as e:
            CustomMethods.log.error("Except block -> switch_to_frame - > not swtiched")

    def switch_to_parent_frame(self):
        try:
            CustomMethods.log.info("Switching to parent frame")
            self.driver.switch_to.default_content()
        except:
            CustomMethods.log.error("Except block -> switch_to_parent_frame - > not swtiched")

    def mouse_hover_element(self, locator, locatortype):
        try:
            CustomMethods.log.info("mouse_hover_element -> "+str(locator)+" -> "+str(locatortype))
            ele = self.getElement(locator, locatortype)
            action = ActionChains(self.driver)
            action.move_to_element(ele).perform()
        except Exception as e:
            CustomMethods.log.error("Except block -> Mouse hover not happened")

    def mouse_hover_click(self, locator, locatortype):
        try:
            CustomMethods.log.info("mouse_hover_element -> " + str(locator) + " -> " + str(locatortype))
            ele = self.getElement(locator, locatortype)
            action = ActionChains(self.driver)
            action.move_to_element(ele).click().perform()
        except Exception as e:
            CustomMethods.log.error("Except block -> mouse_hover_click not happened")