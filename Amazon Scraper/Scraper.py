from bs4 import BeautifulSoup
import requests

class Soup():
    def __init__(self, web_address):
        self.web_address = web_address



    def web_request(self):
        request_call = requests.get(self.web_address)
        web_page = request_call.text
        return web_page
    def soup(self):
        soup = BeautifulSoup(self.web_request(), "html.parser")
        whole_price= soup.find(name= "span", class_="a-price-whole").getText()
        fraction_price= soup.find(name= "span", class_="a-price-fraction").getText()
        full_price = whole_price + fraction_price
        return full_price

URL = "https://www.amazon.com/SAMSUNG-Technology-Intelligent-Turbowrite-MZ-V9S2T0B/dp/B0DHLCRF91/ref=sr_1_10?dib=eyJ2IjoiMSJ9.EoJi2KGtyKkHzukpwyJrsl175r-A3P4yOeGTZX-HRIQlMVreLOsxBv_ykFjm70R2_AudO8cDyEfA_gYNDMXOEudsdrPLTyNdshVE1dtF0z9oWrR1wSAz_lxHSgo7jsY4L5ehHb5VeEFz3idwbRGDofPZozfQI5_Mj4D_AzRYY-G1Ac-TsraZUdR1cVU2XfOOAJxlI1WPEOxNZl_axJKKWvJCAdVWcecH2fyuvuPaUsWHJK-VFJE4Yf_CGvL82WTsxcXzORTU_I__T_MrlNfd0QkulA0rHZxT2Z1kK1TRdLSFTiyF_gYVCth3goVNAxnJEGVeDlrFDBJRv3hQrWWM2-IhRr8yTlmFERGnhEQzbH0.COu_hVYiJhVfuZYbm7Soc3Z8JkxhUBmgwxG5v7X_5V4&dib_tag=se&qid=1736782074&s=computers-intl-ship&sr=1-10&th=1"

obj = Soup(web_address=URL)

obj.soup()
