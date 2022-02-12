from hashlib import new


for i in range(1, 1000):
    num = 125**7 - 25**4 + i
    newNum =''
    base = 5
    while num > 0:
        newNum = str(num%base) + newNum
        num //= base
        if newNum.count('4') == 15 and newNum.count('3') == 1 and newNum.count('1') == 2:
            print(i)
            break
