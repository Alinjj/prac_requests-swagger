import requests
res = requests.delete(f"https://petstore.swagger.io/v2/store/order/666777", data={'apy_key':'6874988345','petId':'55666'})

print(res.text)
print(res.json())
