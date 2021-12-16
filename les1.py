# PEP8

"""
Тут длинный
Очень длинный
Прям на несколько срок
коментарий
"""

#int #integer - целое число
#float #дробное число
#str #string - строка

var_int = 1 # эта строка что-то делает
var_float = 2.222
var_str1 = "Это строка текста 1\nНовая строка"
var_str2 = 'Это строка текста 2'
var_str3 = """Тут 
текст в 
несколько 
строк"""


# while True:
#     user_answer = input('Введите сколько Вам лет: ')
#     if user_answer.isdigit():
#         user_answer = int(user_answer)
#         break
#
#     print('Ошибка ввода. Введено не число.')

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = input("Сколько вам лет? ")
age = int(age)
# result = '{0:^015},\nВам от рождения {2} лет.\nВаша фамилия {1}'.format(name, surname, age)
result = f'{name},\nВам от рождения {age}.\nВы родились в {2021-age} году.\nВаша фамилия {surname}.'

print(result)

# if user_answer >= 18:
#     print("Доступ разрешен во все разделы")
# elif user_answer >= 16:
#     print('Доступ разрешен, но не во все разделы')
# elif user_answer >= 12:
#     print("Можно смотреть мультики")
# else:
#     print("Доступ запрещен")

print('Завершение программы')





