elementcount = int(input('Введите количество элементов списка: '))
while elementcount == 0:
    elementcount = int(input('Введите действительное количество элементов списка (0<): '))
listhomework = []
i = 0
el = 0
g = 1
while i < elementcount:
    gstr = str(g)
    listhomework.append(input('Введите ' + gstr + ' значение списка: '))
    i += 1
    g += 1

for elem in range(int(len(listhomework)/2)):
         listhomework[el], listhomework[el + 1] = listhomework [el + 1], listhomework[el]
         el += 2
print(listhomework)