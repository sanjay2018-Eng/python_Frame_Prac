from utilities.BaseClass import BaseClass


class Test_three(BaseClass):
    def test_create_credit(self):
        self.driver.find_element_by_css_selector("input[id = 'checkBoxOption2']").click()
        print("This is clicking on the checkbox Second")
        ctitle = self.driver.title
        print("entering checkbox "+ctitle)