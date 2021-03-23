acces = 0
name = input('Ваше имя: ')
lastname = input('Введите вашу фамилию: ')
print(name, lastname)
yes_or_not = input('Подтвердите корректность введенных данных (введите да|нет): ')
if yes_or_not == 'да' or 'Да':
    print('Спасибо, данные приняты, вы вошли в систему как: ', name, lastname)
else:
    print('Введите данные снова!')
while acces == 0:
    password = int(input('Введите ваш пароль (5 цифр): '))
    if password == 12345:
        print('пароль введен успешно, вы можете начать работу в системе как: ', name, lastname)
        acces = 1
    else:
        print('Не верный пароль! Попробуйте ще раз!')
        acces = 0
