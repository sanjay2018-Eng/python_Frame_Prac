from time import sleep

from selenium import webdriver
import pytest

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        self.driver.find_element_by_css_selector("input[id='name']").send_keys("Hello")
        log.info("test_e2e_This is printing in the text box_101")
        ctitle = self.driver.title
        log.info("tesst_e2e_entering checkbox_11 " + ctitle)
        self.takescreenshot(self.driver, "Login")
