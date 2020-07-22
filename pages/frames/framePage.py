from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods
from utilities.tables import tableMethods


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

    hideBtn_locator = "input[id='hide-textbox']"
    hideBtn_locatortype = "css"

    showBtn_locator = "input[id='show-textbox']"
    showBtn_locatortype = "css"

    showHideTxtBox_locator = "input[name='show-hide']"
    showHideTxtBox_locatortype = "css"

    tableheader_locator = "//table[@id='product']//tr//th"
    tableheader_locatortype = "xpath"

    tablerows_locator = "//table[@id='product']//tr"
    tablerows_locatortype = "xpath"



    def clickShowBtn(self):
        frame_Page_fields.log.info("clicking on the show Button")
        self.res.clickElement(frame_Page_fields.showBtn_locator, frame_Page_fields.showBtn_locatortype)
        ele = self.res.wait_visiblity_element(frame_Page_fields.showHideTxtBox_locator, frame_Page_fields.showHideTxtBox_locatortype)
        return ele

    def clickHideBtn(self):
        frame_Page_fields.log.info("clicking on the hide Button")
        self.res.clickElement(frame_Page_fields.hideBtn_locator, frame_Page_fields.hideBtn_locatortype)
        ele =self.res.wait_visiblity_element(frame_Page_fields.showHideTxtBox_locator, frame_Page_fields.showHideTxtBox_locatortype)
        return ele

    def enterTxtInShowhideTxtBox(self, text_to_enter):
        frame_Page_fields.log.info("Enter text in show hide Text Box")
        self.res.sendKeysElement(text_to_enter, frame_Page_fields.showHideTxtBox_locator, frame_Page_fields.showHideTxtBox_locatortype)

    def getIndexOfColumns_WebTable(self, colName):
        frame_Page_fields.log.info("Getting the index of columns")
        tMethod = tableMethods(self.driver)
        indexes = tMethod.getColumnIndex(frame_Page_fields.tableheader_locator, frame_Page_fields.tableheader_locatortype)
        colIndex = 0

        for i in indexes.keys():
            if i.lower() == colName.lower():
                colIndex = indexes.get(i)
                break
        return colIndex

    def gettotalRowsIntable(self):
        frame_Page_fields.log.info("Getting the total rows of table")
        tMethod = tableMethods(self.driver)
        rows = tMethod.getTotalrows(frame_Page_fields.tablerows_locator, frame_Page_fields.tablerows_locatortype)
        return rows

    def getCourseName_based_on_price(self, price, colName):
        tMethod = tableMethods(self.driver)
        colIndex = self.getIndexOfColumns_WebTable(colName)
        courseIndex = self.getIndexOfColumns_WebTable("course")
        frame_Page_fields.log.info("Colmun index of --> "+colName+" is --> "+str(colIndex))
        cList = []

        rows = self.gettotalRowsIntable()
        for i in range(2, rows+1):
            x = "//table[@id = 'product']//tr["+str(i)+"]/td[" + str(colIndex) + "]"
            price_text = self.driver.find_element(By.XPATH, x).text
            if int(price_text) == price:
                c = "//table[@id = 'product']//tr["+str(i)+"]/td["+str(courseIndex)+"]"
                courseText = self.driver.find_element(By.XPATH, c).text
                cList.append(courseText)
                frame_Page_fields.log.info("Course with price --> "+price_text+" is --> "+courseText)
        return cList





