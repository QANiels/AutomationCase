from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import requests

#class of the page with the movieList
class MoviePage:

    def __init__(self, driver):
        self.driver = driver

    #coutns the movies listed on the website
    def count_movies(self): #-->int
        totalMovies = self.driver.find_elements(By.CLASS_NAME, "movie__details")
        count = len(totalMovies)
        return count

    #randomly select a movie from the list of movies on the website
    def randomly_select_movie(self):
        movies = self.driver.find_elements(By.CLASS_NAME, "movie__image-container")
        movies[random.randint(0, len(movies))].click()

    #returns a string of the movie title at a specific position on the webpage
    def get_movie_title(self, i): #-->str
        movie = self.driver.find_element(By.XPATH, '/html/body/div/div/main/div/ul/li['+ str(i) + ']/div[2]/h3')
        movie_title = movie.text
        return movie_title

    #returns a boolean value about the status of the movie poster being displayed, based on the position on the website
    def check_movie_posters(self, i): #-->boolean
        images = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/ul/li["+ str(i) +"]/div[1]/div/a/img")

        src = images.get_attribute("src")
        response = requests.get(src)
        if response.status_code == 404:
            return False
        else:
            return True

