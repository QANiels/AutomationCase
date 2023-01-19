from selenium.webdriver.common.by import By

#class called basepage, includes mostly the navigation part of the website. Other pages need to be set up to inherit this page
class BasePage:
    logo_button_class = 'logo'
    SignUp_button_LinkText = 'Sign Up'
    Login_button_linkText = 'Login'
    Profile_button_LinkText = 'Profile'
    Logout_button_LinkText = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    #brings you back to main page
    def go_back_main(self):
        self.driver.find_element(By.CLASS_NAME, self.logo_button_class).click()

    #sents you to sign up
    def go_signup_page(self):
        self.driver.find_element(By.LINK_TEXT, self.SignUp_button_LinkText).click()

    #sends you to login
    def go_login_page(self):
        self.driver.find_element(By.LINK_TEXT, self.Login_button_linkText).click()

    #sends you to profile
    def go_profile_page(self):
        self.driver.find_element(By.LINK_TEXT, self.Profile_button_LinkText).click()

    #logs you out
    def logout(self):
        self.driver.find_element(By.LINK_TEXT, self.Logout_button_LinkText).click()