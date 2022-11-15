import requests

res = requests.put(f"petstore.swagger.io/v2/user/igor", data={
  "id": 555,
  "username": "jpnh",
  "firstName": "h",
  "lastName": "g",
  "email": "dead7341us@mail.com",
  "password": "123",
  "phone": "444555",
  "userStatus": 8
})
print(res.status_code)
print(res.text)
print(res.json())