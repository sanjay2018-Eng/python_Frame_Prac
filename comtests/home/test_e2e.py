from time import sleep

from selenium import webdriver
import pytest

from pages.home.login_page import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        hPage = HomePage(self.driver)
        hPage.enterDataInAlertBox("Hello Data1")
        log.info("Entered the data in alert Text box")

