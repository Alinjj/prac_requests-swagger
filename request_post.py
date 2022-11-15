import requests
res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json'}, data={"id": 777624,"name": "doggie","status":"available"})

print(res.status_code)
print(res.text)
print(res.json())