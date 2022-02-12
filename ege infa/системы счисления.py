# Просто переписываем пример в переменную num

num = 652

# Цикл обработки примера, выводит в конце число, в котором ищем нужную нам цифру и ее кол-во
for i in range(2, 11):
    base = i
    numm = num
    newNum = ''
    while numm > 0:
        newNum = str(numm % base) + newNum
        numm //= base
    print(i, newNum)



