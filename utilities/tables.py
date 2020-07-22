from utilities.BaseClass import BaseClass
from utilities.reusablemethods import CustomMethods


class tableMethods():
    log = BaseClass().getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.res = CustomMethods(self.driver)

    def getColumnIndex(self, locator, locatortype):
        try:
            tableMethods.log.info("table methods locator --> "+locator+"locator type -> "+locatortype)
            tableColumn = {}
            col = self.res.getElements(locator, locatortype)
            index = 1
            for c in col:
                tableColumn[c.text] = index
                index = index+1
            return tableColumn
        except:
            tableMethods.log.info("Except block -> get Column index table methods")

    def getTotalrows(self, locator, locatortype):
        try:
            tableMethods.log.info("table methods locator --> " + locator + "locator type -> " + locatortype)
            tableMethods.log.info("Getting total rows")
            rows = self.res.getElements(locator, locatortype)
            tableMethods.log.info("total rows is --> "+str(len(rows)))
            return len(rows)
        except Exception as e:
            tableMethods.log.info("Except block -> get Column index table methods")
            tableMethods.log.info(e)