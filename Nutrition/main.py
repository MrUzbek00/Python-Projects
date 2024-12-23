import requests
from datetime import datetime

NUTRITION_ID ="" #Nutrition ID
NUTRITION_API_KEY = "" #Nutrition Key
NUTRITION_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITION_TOKEN = ""#Nutrition Token

#Your personal data
GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 184
AGE = 25


HEAEDER = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API_KEY, 
    "Authorization":f"Basic {NUTRITION_TOKEN}"
}

exercise_text = input("Which exercises did you do?")

parameter={
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


api_call = requests.post(url=NUTRITION_API, json=parameter, headers=HEAEDER)
data = api_call.json()
#print(data)


MY_WORK_OUT_ENDPOINT = "" #Get your API from Sheety 

today = datetime.now()

for c in range(len(data["exercises"])):
    exercise = data["exercises"][c]["user_input"]
    duration = data["exercises"][c]["duration_min"]
    calories = data["exercises"][c]["nf_calories"]
    
    body = {"sheet1": {
        "date": today.strftime("%d/%m/%Y"), 
        "time": today.strftime("%H:%M:%S"), 
        "exercise": exercise.title(), 
        "duration": duration, 
        "calories": calories,
    }, 
}

    input_call = requests.post(url=MY_WORK_OUT_ENDPOINT, json=body, headers=HEAEDER)
    input_call.raise_for_status()
#print(input_call)
