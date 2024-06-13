import pprint
import requests
import json

url_SW = "https://swapi.dev/api/people/"

url = "https://fakestoreapi.com/users"

fio = input('О каком пользователе Вы хотите получить информацию?:  ')
response = requests.get(url).json()
print(response)
flag = False
for item in response:
    print(item['name']['lastname'])
    if item['name']['lastname'] == fio:
        print(f'Имя: {item["name"]["firstname"]} Фамилия: {item["name"]["lastname"]}')
        print(f'Телефон: {item["phone"]}\nEmail: {item["email"]}')
        flag = True

if not flag:
    print(f'Нет такого пользователя')
