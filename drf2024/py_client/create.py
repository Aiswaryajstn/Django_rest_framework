import requests


headers = {
   'Authorization': 'Bearer f53b9c0cd9d86040b005a7091f055fa09ee903fb'
}
endpoint = "http://localhost:8000/api/products/"

data = {
   "title" : "This field is almost done",
   "content": "good",
   "price" : 42
}

get_response = requests.post(endpoint, json = data, headers= headers)
print(get_response.json())