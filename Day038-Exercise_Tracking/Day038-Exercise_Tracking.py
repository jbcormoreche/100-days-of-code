# Day 38 Project - Exercise Tracking

import requests
from datetime import datetime
import os

GENDER = "YOUR_GENDER"
WEIGHT_KG = "YOUR_WEIGHT"
HEIGHT_CM = "YOUR_HEIGHT"
AGE = "YOUR_AGE"

APP_ID = os.environ["YOUR_APP_ID"]
API_KEY = os.environ["YOUR_API_KEY"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["YOUR_SHEET_ENDPOINT"]

exercise_text = input("Tell me what exercises you did: ")

exercises_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercises_params, headers=headers)
result = response.json()
print(result)

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%X")

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

    # No Authentication
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["USERNAME"],
            os.environ["PASSWORD"],
        )
    )

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
