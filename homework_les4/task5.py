from functools import reduce

def my_func(prev_el, el):
    return prev_el * el


my_list = []

for el in range(100, 1001, 2):
    my_list.append(el)

print(reduce(my_func, my_list))

