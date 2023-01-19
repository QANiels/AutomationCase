from selenium import webdriver
from selenium.webdriver.common.by import By

#contains elements and functions of the Login page
class LoginPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "/html/body/div/div/form/section/button"
    button_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    #fill in username field
    def setUsername(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    #fill in password field
    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    #clicks login button
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    #clicks logout button
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_linktext).click()