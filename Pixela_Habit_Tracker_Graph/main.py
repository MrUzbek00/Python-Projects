#working with pexe.la api
#working on other advanced methods of HTTPs
import requests
from datetime import datetime 
TOKEN = " " #Pixela Token
USERNAME = " " #Pixela Username

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes", 
    "notMinor": "yes", 

}

# resposnse = requests.post(url=pixela_endpoint, json=user_param)
# print(resposnse.text)

graph_config = {
    "id": "graph1", 
    "name": "Programming", 
    "unit": "Minusts",
    "type": "float", 
    "color": "sora",

}

headers={
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

# resposnse = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(resposnse.text)
#Creating a pixal on pixela graph
today = datetime.now()
print(today.strftime("%Y%m%d"))

post_config = {
    "date": today.strftime("%Y%m%d"), 
    "quantity":"520"
}


post_pixal_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

# resposnse = requests.post(url=post_pixal_endpoint, json=post_config, headers=headers)
# print(resposnse.text)

#Updating pixel in a graph
update_pixal_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/20241201"

update_config = {
    "quantity": "250"
}

resposnse = requests.put(url=update_pixal_endpoint, json=update_config, headers=headers)
print(resposnse.text)

