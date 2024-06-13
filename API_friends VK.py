import requests
import json
import time

access_token ="vk1.a.uvHtRCB7EvCQkZvOjlv5ZukrQ9EztJURWj9uTrmTtnEezlOLgYkgpwRCbOKGvSiWnEy4v2rwqt17dNWfYOqVWhLK-Govqe90rCX2JfYxBzAi0Ra3j2SlEQwxvA_tDlKSZC4oEB4-8WgGl-BtLv29qCY-yfvzAB-ZKNoghjN6auHzOiacbQDI0IVgPa1HJs9S"
#input('токен')
user_input = 529066920  #input("Введите идентификатор или ник VK: ")
url = "https://api.vk.com/method/friends.get"
params = {"user_ids": user_input,"fields": "city,last_seen,status",
"access_token": access_token,"v": "5.131","order": "name"}

response = requests.get(url, params=params)
#print(response.text)
user_info = response.json()['response']
#print(response.json())

print("Мои друзья - ", user_info['count'],':\n')

q=user_info['count']
for i in range(q+1):
    print("Имя:", user_info['items'][i]["first_name"])
    print("Фамилия:", user_info['items'][i]["last_name"])
    print("Статус:", user_info['items'][i]["status"])
    unix_timestamp = user_info['items'][i]["last_seen"]['time']
    time_struct = time.gmtime(unix_timestamp)
    print("Последний вход в сеть:",time.strftime("%B %d %Y", time_struct))
    print('*'*50)
    
    
