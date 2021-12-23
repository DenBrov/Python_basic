import os

file_path = os.path.join(os.path.dirname(__file__), '../homework_les3/test.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    size = len([0 for _ in file])
    print(size)