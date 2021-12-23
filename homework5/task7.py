import os
import json

file_path = os.path.join(os.path.dirname(__file__), '../homework_les3/test_3.txt')
db_dict = {}
with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        data = line.split()
        name = data[0]
        val = int(data[2]) - int(data[3])
        if val > 0: db_dict[name] = int(val)
    aver = sum(db_dict.values()) / len(db_dict)
    db_dict['average'] = int(aver)
    end_list = [db_dict]


with open('../homework_les3/profit.json', 'w') as profit:
    json.dump(end_list, profit)