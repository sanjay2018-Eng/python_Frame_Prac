from pages.frames.framePage import frame_Page_fields
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods
from utilities.tables import tableMethods


class Test_Tablevalidation(BaseClass):
    def test_validate_price_in_table(self):
        log = self.getLogger()
        log.info("\n*** Test Case - test_validate_price_in_table ***\n")
        framePage = frame_Page_fields(self.driver)
        listC = framePage.getCourseName_based_on_price(30, "price")
        expectedCourse = "Appium (Selenium) - Mobile Automation Testing from Scratch"
        if expectedCourse in listC:
            log.info("Course Present")
            assert True
        else:
            log.info("Course not Present")
            assert False

