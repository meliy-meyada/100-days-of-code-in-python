import requests
from datetime import datetime
import os


GENDER = "female"
WEIGHT_KG = 65
HEIGHT_CM = 165
AGE = 24

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
TOKEN = os.environ.get('TOKEN')



exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get('SHEET_ENDPOINT')
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)