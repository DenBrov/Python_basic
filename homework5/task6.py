import os

file_path = os.path.join(os.path.dirname(__file__), '../homework_les3/test_2.txt')
db_dict = {}
with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        data = line.split(' ')
        name = data[0].split(':')[0]
        db_dict[name] = data[1:]

result = {}
for key, value in db_dict.items():
    result[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])
print(result)