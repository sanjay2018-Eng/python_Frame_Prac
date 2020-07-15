from utilities.BaseClass import BaseClass


class Test_two(BaseClass):
    def test_create_credit(self):
        self.driver.find_element_by_css_selector("input[id = 'checkBoxOption1']").click()
        print("This is clicking on the checkbox first")
        ctitle = self.driver.title
        print("entering checkbox "+ctitle)
        print("Added by sec")
        print("Added by original user")
        print("Parallel testing")

    def test_in_develop_branch_credit(self):
        print("This is in develop branch in credit method")