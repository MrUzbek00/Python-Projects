from bs4 import BeautifulSoup
import requests
# date  = input("Which year would tyou like to travel to? Please enter year in the following format YYYY-MM-DD")

class SongScraper():
    def __init__(self, date):
        self.date = date

    def SongList(self):
        URL = f"https://www.billboard.com/charts/hot-100/{self.date}/"
        request_call = requests.get(URL)
        web_page = request_call.text
        soup = BeautifulSoup(web_page, "html.parser")
        #all_tags_h3 = soup.select(selector="li h3")
        all_tags_h3 =soup.find_all(name="h3", class_="a-no-trucate")
        song_list = []
        for h3 in all_tags_h3:
            song_name =(h3.getText().strip())
            if len(song_list) <100:
                song_list.append(song_name)
            else:
                break
        return song_list