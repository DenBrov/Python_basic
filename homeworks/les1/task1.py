sec = int(input('Введите количество секунд: '))
hour = sec // 3600
min = (sec - hour * 3600) // 60
sec = sec % 60
if hour < 0: hour = 0
if min < 0: min = 0

print(f"Введенное количество секунд равно: {hour} часов {min} минут {sec} секунд")

