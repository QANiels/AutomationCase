from selenium.webdriver.common.by import By

#class for the detail page of the movies
class MovieDetails:
    title_element_XPATH = '//*[@id="app"]/div/main/dl/dt[1]'
    genre_element_XPATH = '//*[@id="app"]/div/main/dl/dt[2]'
    year_element_XPATH = '//*[@id="app"]/div/main/dl/dt[3]'

    def __init__(self, driver):
        self.driver = driver

    #search for the title element
    def check_title_present(self):
        self.driver.find_element(By.XPATH, self.title_element_XPATH)

    #search for the genre element
    def check_genre_present(self):
        self.driver.find_element(By.XPATH, self.genre_element_XPATH)

    #search for the year element
    def check_year_present(self):
        self.driver.find_element(By.XPATH, self.year_element_XPATH)

    #returns a string of the title
    def get_title(self): #-->str
        return self.driver.find_element(By.XPATH, self.title_element_XPATH).text

    #returns a string of the year
    def get_year(self): #-->str
        return self.driver.find_element(By.XPATH, self.year_element_XPATH).text

    #returns a string of the genre
    def get_genre(self): #-->str
        return self.driver.find_element(By.XPATH, self.genre_element_XPATH).text



