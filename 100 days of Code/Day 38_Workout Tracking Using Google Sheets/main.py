import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 93
HEIGHT_CM = 160
AGE = 20

os.environ["APP_ID"] = "4f69f575"
APP_ID = os.environ.get("APP_ID")


os.environ["API_KEY"] = "18d6a7646fc4899291baa5f1ab8ee259"
API_KEY = os.environ.get("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

os.environ["SHEET_ENDPOINT"] = "https://api.sheety.co/a7adbeb53504d5346f57386f055984d7/myCardioChart/workouts"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

os.environ["USERNAME"] = "danhhoa"
os.environ["PASSWORD"] = "ndh2912001"
os.environ["TOKEN"] = "ndh2912001!"

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
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

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

    #No Auth
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    # #Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint, 
    #     json=sheet_inputs, 
    #     auth=(
    #         os.environ.get("USERNAME"), 
    #         os.environ.get("PASSWORD")
    #     )
    # )

    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )

    print(sheet_response.text)
