import requests

endpoint = "http://localhost:8000/api/products/2/"

get_response = requests.get(endpoint)
print(get_response.json())










# endpoint = "http://localhost:8000/api/"
#### get#####
# get_response = requests.get(endpoint, json={"query":"hello"})
#####post#####
# get_response = requests.post(endpoint, json= {"content" : "awesome day"})
#print(get_response.headers)
#print(get_response.text)
# print(get_response.json())
# print(get_response.status_code )