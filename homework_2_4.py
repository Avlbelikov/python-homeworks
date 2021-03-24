string = input('Введите данные через пробел: ')
word = []
number = 1
for el in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f' {number} {word [el]}')
        number += 1
    else:
        print(f' {number} {word [el] [0:10]}')
        number += 1