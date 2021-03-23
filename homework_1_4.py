n_cell = int(input('Введите целочисленное положительное число: '))
a = n_cell % 10
a = a // 10
while n_cell > 0:
    if n_cell % 10 > a:
        a = n_cell % 10
    n_cell = n_cell // 10
print(a)