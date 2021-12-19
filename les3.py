def my_enumerate(a, *args, **kwargs) -> list:
    """Моя реализация функции enumerate
    :param data: list
    :param start: int
    :return: list (num, item)
    """
    print(kwargs)
    print(a)
    print(type(args))

    start = kwargs.get('start', 0)
    result = []
    for itm in args:
        result.append((start, itm))
        start += 1
    return result

def my_temp(data: list):
    data.append('1652')
    return data

def my_sum(data: list):
    result = 0
    for itm in data:
        result += itm
    return result

print(my_sum([1,2,3]))


a = ['Hello', 'my', 'dear', 'friends']

data = [a, 2]
data2 = {
    'data': a,
    'start': 3
}

res = my_enumerate(1, 2 ,3 ,4 ,5, 6, 7, 8, start=17, end=22, hello=33)
# print(a)
# res = my_temp(a)
# print(res)
print("#" * 30)
print(a)
print(res)
