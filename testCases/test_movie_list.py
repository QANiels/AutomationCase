import pytest
from selenium import webdriver
from pageObjects.MoviePage import MoviePage
from pageObjects.MovieDetails import MovieDetails
import requests

class Test_001_MovieList:
    base_url = 'http://localhost/movies'

    #test to check if the number of movies on imtb matches those in the API
    def test_number_of_movies(self, setup):
        #set up driver and pageObjects
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        mp = MoviePage(self.driver)
        #count movies on website
        listed_movies = mp.count_movies()
        self.driver.implicitly_wait(10)
        self.driver.close()
        #count movies in API
        response = requests.get("http://localhost:4243/api/movies")
        data = response.json()
        movies_api = len(data)
        assert listed_movies == movies_api

    #Test to see if the API and the website have the same movies and in the same order
    def test_correct_movies(self, setup):
        #set up drivers and pageObjects
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        mp = MoviePage(self.driver)
        #get number of movies on the page for iteration
        number = mp.count_movies()
        self.driver.implicitly_wait(10)
        #Grab movie information from the API
        response = requests.get("http://localhost:4243/api/movies")
        data = response.json()
        #two lists are created that will contain titles from the website or the API
        web_movie = []
        api_movie = []
        #For loop that iterates through both the website and the JSON from the API and adds them to their respective lists
        for i in range(number):
            api_movie.append(data[i]['title'])
            web_movie_num = i+1
            web_movie.append(mp.get_movie_title(web_movie_num))

        assert web_movie == api_movie
        self.driver.close()

    #Test for selecting movies from the list and see if it redirects you to the correct place
    def test_movie_selection(self, setup):
        #set up driver and pageObjects
        self.driver = setup
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        mp = MoviePage(self.driver)
        #select a random movie and see if the redirect works correctly
        mp.randomly_select_movie()
        md = MovieDetails(self.driver)
        assert md.check_title_present()
        self.driver.close()

    #Test which checks if all movie posters are displayed correctly
    def test_movie_posters(self, setup):
        #set up the driver and page objects
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        mp = MoviePage(self.driver)
        #grab number of movies for the iteration
        number = mp.count_movies()
        self.driver.implicitly_wait(10)
        #list for adding boolean values
        present = []
        #for loop that loops through all movies on the page and adds a boolean about the image loading correctly
        for i in range(number):
            num = i + 1
            present.append(mp.check_movie_posters(num))
        assert all(present)
        self.driver.close()
