from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods


class frame_Page_fields():
    log = BaseClass().getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.res = CustomMethods(self.driver)

    #*** Locators ***

    earn_locator = "//a[text()='Earn']"
    earn_locatortype = "xpath"
    
    mousehoverBtn_locator = "mousehover"
    mousehoverBtn_locatortype = "id"

    hover_menu_locator = "//div[@class='mouse-hover-content']"
    hover_menu_locatortype = "xpath"

    hover_topmenu_locator = "//a[text()='Top']"
    hover_topmenu_locatortype = "xpath"






