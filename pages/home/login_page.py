from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    #Locators
    _login_link_locator = "Login"
    _login_link_type = "LINK_TEXT"

    email_locator = "user_email"
    email_type = "ID"

    password_locator = "user_password"
    password_type = "ID"

    login_Button = "input[value='Log In']"
    loginBtn_type = "CSS"

    def getLoginlink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link_locator)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self.email_locator)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self.password_locator)

    def getLoginButton(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.login_Button)

    def clickLoginLink(self):
        self.getLoginlink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()