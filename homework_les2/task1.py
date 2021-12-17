my_list = input('Введите данные: ')
my_list = list(my_list)
if len(my_list) % 2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    print(" ".join(i for i in my_list))
else:
    my_list[:-1:2], my_list[1:-1:2] = my_list[1:-1:2], my_list[:-1:2]
    print(" ".join(i for i in my_list))



