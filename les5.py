import os
from os import path
import json
import requests
#
# file_name = 'test_les.txt'
# file_path = path.join(path.dirname(__file__), file_name)
#
# print(__file__)
# print(file_path)
#
# print(os.listdir(path.dirname(__file__)))
#
# print(path.isdir(path.dirname(__file__)))
#
# # for itm in os.listdir(path.dirname(__file__)):
# #     print(itm, path.isdir(path.join(path.dirname(__file__),itm)))
#
# os.remove(file_path)
#
# # file = open('test_les.txt', 'r', encoding='UTF-8')
#
# # data = [f'tap - {num}\n' for num in range(100)]
# #
# # for itm in data:
# #     file.write(itm)
#
# # for itm in file:
# #     print(itm, end='')
#
# # print(file.read(8))
# # print(file.read(8))
# # try:
# #     pass
# # except IOError as e:
# #     pass
# # finally:
# #     file.close()
#
# # with open('test_les.txt', 'r', encoding='UTF-8') as file,\
# #         open('test_les_2.txt', 'w', encoding='UTF-8') as file_2:
# #
# #     for itm in file:
# #         file_2.write(itm)

# users = [
#     {'name': 'user_1', 'surname': 'sur_1', 'age': 22},
#     {'name': 'user_2', 'surname': 'sur_2', 'age': 33},
#     {'name': 'user_3', 'surname': 'sur_3', 'age': 44},
#     'hello',
#     True,
#     (1,2,3,4),
#     None
# ]
#
# j_data = json.dumps(users)
# print(type(j_data))
# print(j_data)
#
# with open('data', 'w', encoding = 'UTF-8') as file:
#     json.dump(users, file)

# print(type(data))
# print(data)
url = 'https://5ka.ru/api/v2/special_offers/'
photo = 'https://media.5ka.ru/media/products/3644078.jpg'
response = requests.get(photo)


with open('ph.jpg', 'wb') as file:
    file.write(response.content)

# print(response.json())
# data = response.json()
# for itm in data['results']:
#     print(itm)