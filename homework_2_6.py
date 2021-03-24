total_input = int(input("Сколько наименований вы хотите ввести: "))
i = 1
dict_product = []
list_product = []
analitik_product = {}
while i <= total_input:
    dict_product = dict({'Название': input("Введите название: "), 'Цена': input("Введите цену: "),
                         'Количество': input('Введите количество '), 'Ед.': input("Введите единицу измерения: ")})
    list_product.append((i, dict_product))
    i += 1
    analitik_product = dict({'Название': dict_product.get('Название'), 'Цена': dict_product.get('Цена'),
                             'Количество': dict_product.get('Количество'), 'Ед.': dict_product.get('Ед.')})
print(list_product)
print(analitik_product)
