with open("../homework_les3/my_file.txt", 'w', encoding='UTF-8') as file:

    while True:
        inp = input('Введите текст:')
        if not inp:
            break
        file.write(f'{inp}\n')
