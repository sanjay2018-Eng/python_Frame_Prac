from utilities.BaseClass import BaseClass


class Test_two(BaseClass):
    def test_create_credit(self):
        log = self.getLogger()
        self.driver.find_element_by_css_selector("input[id = 'checkBoxOption1']").click()
        log.info("credit_This is clicking on the checkbox first_1")
        ctitle = self.driver.title
        log.info("credit_entering checkbox_2 "+ctitle)
        log.warning("credit_Added by sec_3")
        log.info("credit_Added by original user_4")
        log.info("credit_Parallel testing_5")

    def test_in_develop_branch_credit(self):
        log = self.getLogger()
        log.info("credit_This is in develop branch in credit method_6")
        log.info("credit_Added by Original_7")