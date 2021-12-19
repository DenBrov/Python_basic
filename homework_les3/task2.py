def user_data():
        name = input('введите свое имя: ')
        surname = input('введите свою фамилию: ')
        year = input('введите свой год рождения: ')
        city = input('введите свой город проживания: ')
        mail = input('введите адрес своей электронной почты: ')
        phone = input('введите свой номер телефона: ')
        full_string = f'Имя: {name}, фамилия: {surname}, год рождения: {year}, город: {city}, эл. почта: {mail},телефон: {phone}.'
        return full_string

print(user_data())