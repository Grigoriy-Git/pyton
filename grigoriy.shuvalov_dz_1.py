duration = input('Введите число: ')
if duration.isdigit():
    duration = int(duration)
    print(duration // 3600, duration // 60 % 60, duration % 60)
else:
    print('Вы ввели не число!')