import requests
from datetime import datetime

USERNAME = "nguyendanhhoa"
TOKEN = "nguyendanhhoa20012001"
GRAPH_ID = "graph1"
#Create a user account
"""$ curl -X POST https://pixe.la/v1/users -d '
 {"token":"thisissecret", "username":"a-know", 
 "agreeTermsOfService":"yes", "notMinor":"yes"}'
 """

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


#CREATE GRAPH----------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name": "Running Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


#ADD VALUE FOR PIXEL----------------------------------
pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

QUANTITY = float(input("How many kilometers do you run today? "))

today = datetime.now()

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : str(QUANTITY)
}

response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)



#UPDATE DISTANCE----------------------------
# update_endpoint = f"{pixela_creation_endpoint}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#     "quantity": "0"
# }

# ## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)



#DELETE PIXEL------------------------------
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
