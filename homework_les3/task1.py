def division(num1, num2):

    try:
        x = float(num1) / float(num2)
    except ValueError as e:
        print('Введено не число')
        return
    except ZeroDivisionError as e:
        print('Деление на ноль')
        return
    return(x)

num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
print(division(num1, num2))