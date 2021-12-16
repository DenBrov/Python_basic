num = input('Введите число: ')
x = 0

while num:
    if int(num) % 10 > x:
        x = int(num) % 10
    else:
        x = x
    num = int(num) // 10

print(x)