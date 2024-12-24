from bs4 import BeautifulSoup
import requests

class Scraper():
    def __init__(self):
        self.movie_list = []
    def scraper(self):
        response =  requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
        web_page =response.text
        soup = BeautifulSoup(web_page, "html.parser")
        all_h3_tags= soup.find_all(name="h3", class_="title")
        return all_h3_tags
    def movie_list_func(self):
        tags =self.scraper()
        for tag in tags[::-1]:
            text =tag.getText().replace(":", ")")
            movie = text.split(")")
            self.movie_list.append(movie[1])
        return self.movie_list
    


