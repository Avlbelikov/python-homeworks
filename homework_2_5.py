list1 = [7, 5, 3, 3, 2]
print(f'Рейтинг - {list1}')
rait = int(input('Введите значение: '))
while rait != 0:
    for el in range(len(list1)):
        if list1[el] == rait:
            list1.insert(el + 1, rait)
            break
        elif list1[0] < rait:
            list1.insert(0, rait)
        elif list1[-1] > rait:
            list1.append(rait)
        elif list1[el] > rait and list1[el + 1] < rait:
            list1.insert(el + 1, rait)
    print(f'Текущий рейтинг - {list1}')
    rait = int(input('Введите значение: '))