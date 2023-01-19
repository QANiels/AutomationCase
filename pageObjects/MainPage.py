from selenium.webdriver.common.by import By

#class contains elements and functions of the homepage
class MainPage:
    MovieList_button_XPATH = '/html/body/div/div/section/button'

    def __init__(self, driver):
        self.driver = driver

    #button to click to go to movie list
    def go_to_Movie_list(self):
        self.driver.find_element(By.XPATH, self.MovieList_button_XPATH).click()