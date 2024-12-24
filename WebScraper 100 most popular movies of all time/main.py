from scraper import Scraper
from create_file import CreateCSV

#Scrapes a website for the 100 movies
movie_list = Scraper()

#creates a list of movies
movie_list.movie_list_func() 

#gets the list and creates Txt or CSV file
CSV_file = CreateCSV(movie_list=movie_list)
CSV_file.create_csv_file()