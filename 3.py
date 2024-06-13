import requests
r=requests.get('https://fakestoreapi.com/products/1').json()
print(r)