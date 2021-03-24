list_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
dict_seasons = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
i = 1
while i > 0:
    month = int(input('Введите номер месяца: '))
    if month ==12 or month == 1 or month == 2:
        print('Решение через dict: ', dict_seasons.get(1))
        print('Решение через list: ', list_seasons[0])
        i = 0
    elif month == 3 or month == 4 or month ==5:
        print('Решение через dict: ', dict_seasons.get(2))
        print('Решение через list: ', list_seasons[1])
        i = 0
    elif month == 6 or month == 7 or month == 8:
        print('Решение через dict: ', dict_seasons.get(3))
        print('Решение через list: ', list_seasons[2])
        i = 0
    elif month == 9 or month == 10 or month == 11:
        print('Решение через dict: ', dict_seasons.get(4))
        print('Решение через list: ', list_seasons[3])
        i = 0
    else:
        print('Такого месяца не существует!')
        i += 1