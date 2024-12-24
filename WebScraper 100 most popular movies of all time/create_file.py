from scraper import Scraper
import pandas as pd
#print(movie_list)
class CreateTxt():
    def __init__(self, movie_list):
        self.movie_list = movie_list

    def  create_txt_file(self):
        with open("All Time 100 Movies.txt", "w", encoding="utf-8") as file:
            for movie in self.movie_list:
                file.writelines(str(movie,))
                file.write("\n")
class CreateCSV():
    def __init__(self, movie_list):
        self.movie_list = movie_list
    
    def data_frame(self):
        data = []
        for index, movie in enumerate(self.movie_list, start = 1):
            data.append({"No":index, "Movies": movie})
        df = pd.DataFrame(data)
        return df
    def create_csv_file(self):
        df = self.data_frame()
        df.to_csv("All Time 100 Movies.csv", index=False)
