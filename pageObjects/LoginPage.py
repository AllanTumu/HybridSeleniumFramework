class LoginPageElements:
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    login_button_xpath = "//input[@class='button-1 login-button']"
    logout_link_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()
