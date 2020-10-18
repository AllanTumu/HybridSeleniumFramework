import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPageElements
from testCases.configtest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("----------------------- Test_001_Login --------------------")
        self.logger.info("****************** Verifying Home page Title ******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************** Home page title Passed ******************")

        else:
            self.driver.save_screenshot('../screenShots/test_homePageTitle.png')
            self.driver.close()
            self.logger.error("****************** Home Page title Failed ******************")
            assert False

    def test_Login(self, setup):

        self.logger.info("************************* Initializing the Successful Login Tests ***********************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPageElements(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        page_title = self.driver.title

        print(page_title)
        if page_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("****************** Log in test title Passed ******************")
        else:
            self.driver.save_screenshot('../screenShots/test_Login.png')
            self.driver.close()
            self.logger.error("****************** Log in test title failed ******************")
            assert False
