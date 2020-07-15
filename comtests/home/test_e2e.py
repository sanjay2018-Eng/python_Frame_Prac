from time import sleep

from selenium import webdriver
import pytest

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.find_element_by_css_selector("input[id='name']").send_keys("Hello")
        print("This is printing in the text box")
        ctitle = self.driver.title
        print("entering checkbox " + ctitle)
