from utilities.BaseClass import BaseClass


class Test_three(BaseClass):
    def test_create_debit(self):

        log = self.getLogger()
        self.driver.find_element_by_css_selector("input[id = 'checkBoxOption2']").click()
        log.info("debit_This is clicking on the checkbox Second_12")
        ctitle = self.driver.title
        log.info("debit_entering checkbox_13 "+ctitle)
        log.info("debit_Added by original user_14")
        log.info("debit_Serial testing_15")

    def test_in_develop_branch_debit(self):
        log = self.getLogger()
        log.info("debit_This is in develop branch in debit method_16")