import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.BasePage import BasePage
from pageObjects.SignUpPage import SignUpPage
from selenium.webdriver.common.by import By


class Test_002_Login:
    base_url = "http://localhost/"
    username1 = "testing12"
    password1 = "1234"
    failed_login_XPATH = '/html/body/div/div/section/h2'

    #Test for signing up to the website
    def test_sign_up(self, setup):
        #Set up driver and pageObjects
        self.driver = setup
        self.driver.get(self.base_url)
        bp = BasePage(self.driver)
        sp = SignUpPage(self.driver)
        bp.go_signup_page()
        self.driver.implicitly_wait(10)
        #process of creating user
        sp.setUsername(self.username1)
        sp.setPassword(self.password1)
        sp.clickSignUp()
        self.driver.implicitly_wait(10)
        #search for username on the page you get sent after signing up
        name = self.driver.find_element(By.XPATH, '/html/body/div/div/main/dl/dd').text
        self.driver.close()
        assert name == self.username1

    #test to check the behavior with a succesfull login
    def test_login(self, setup):
        #set up drivers and pageObjects
        self.driver = setup
        self.driver.get(self.base_url)
        bp = BasePage(self.driver)
        lp = LoginPage(self.driver)
        bp.go_login_page()
        #login process
        lp.setUsername(self.username1)
        lp.setPassword(self.password1)
        lp.clickLogin()
        self.driver.implicitly_wait(10)
        #check if profile is now available
        assert self.driver.find_element(By.LINK_TEXT, 'Profile')
        self.driver.close()

    #test to see if correct behavior is present when the wrong password is uploaded
    def test_login_wrong_password(self, setup):
        #set up driver and pageObjects
        self.driver = setup
        self.driver.get(self.base_url)
        bp = BasePage(self.driver)
        lp = LoginPage(self.driver)
        bp.go_login_page()
        #login process
        lp.setUsername(self.username1)
        lp.setPassword("hackathon")
        lp.clickLogin()
        self.driver.implicitly_wait(10)
        #check if the login failed page is reached
        page_title = self.driver.find_element(By.XPATH, self.failed_login_XPATH).text
        self.driver.implicitly_wait(10)
        self.driver.close()
        assert page_title == "Login Failed"
