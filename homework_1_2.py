second_in = int(input('Введите количество секунд: '))
hour = second_in // 3600
minute = (second_in // 60) % 60
second = second_in % 60
if hour <= 9:
    hourHH = '0' + str(hour)
else:
    hourHH = str(hour)
if minute <= 9:
    minuteMM = '0' + str(minute)
else:
    minuteMM = str(minute)
if second <= 9:
    secondSS = '0' + str(second)
else:
    secondSS = str(second)
print('Введенные вами секунды в формате ЧЧ:ММ:СС: '+hourHH+':'+minuteMM+':'+secondSS)