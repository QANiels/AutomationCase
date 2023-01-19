from selenium.webdriver.common.by import By

#behavior and elements of the Sign Up page
class SignUpPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    textbox_repeat_password_id = "repeat-password"
    SignUp_button_XPATH = '/html/body/div/div/form/section/button'

    def __init__(self, driver):
        self.driver = driver

    #adding value to the username field
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    #adding value to the password and password confirmation field
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        self.driver.find_element(By.ID, self.textbox_repeat_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_repeat_password_id).send_keys(password)

    #clicking signup button
    def clickSignUp(self):
        self.driver.find_element(By.XPATH, self.SignUp_button_XPATH).click()
