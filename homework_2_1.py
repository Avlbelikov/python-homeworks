homeworklist = [True, 'Имя', 5, 4.3, tuple('кортеж')]
def my_type(el):
    for el in range(len(homeworklist)):
        print(type(homeworklist[el]))
    return
my_type(homeworklist)
