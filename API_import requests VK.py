import requests
import json

# Ваш персональный access_token для доступа к API VK

access_token = 'vk1.a.EN0pRn2t25AmyLrBQzkmphBHVMvnc94ZGzxSW99vX2lgx0VO3FByrUG38tKOG2X8QtE5B_YHTPhWkSWadET9E7sqjt0h94vSng5QtrCw7ys999XKUzzbALzKQL21i0Oa8sRDmBNMM5p-JEXtmg0j8XU4PIoJOLwwtQjQgTZdCS5jqBSHaYO7t_4WGTLQf7_7'

# Запрашиваем у пользователя идентификатор или ник VK

user_input = input("Введите идентификатор или ник VK: ")

# Формируем URL для запроса

url = "https://api.vk.com/method/users.get"

# Параметры запроса и их значения

params = {

# Идентификатор или ник VK пользователя

"user_ids": user_input,

# Список полей, которые необходимо получить

"fields": "city,career",

# Ваш access_token

"access_token": access_token,

# Версия API

"v": "5.131"

}

# Отправляем GET-запрос

response = requests.get(url, params=params)

# Получаем ответ в формате JSON

user_info = response.json()["response"][0]

# Выводим информацию о пользователе в читабельном виде

print("Имя:", user_info["first_name"])

print("Фамилия:", user_info["last_name"])

print("Город:", user_info["city"]["title"])

print("Карьера:")

# Итерируемся по истории работы пользователя

for job in user_info["career"]:
    try:
        
# Пытаемся вывести информацию о каждой позиции
        print(f"Должность: {job['position']}; ", end = '')
        print(f"С {job['from']} ", end = '')

        print(f"по {job['until']}; ", end = '')

        print(f"Компания: {job['company']}", end = '')

    except KeyError:

# Если не вся информация о позиции заполнена, выводим сообщение

        print("Не вся информация о позиции заполнена")