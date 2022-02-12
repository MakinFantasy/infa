from itertools import permutations

counter = 0
s = True

a = ['С','В','Е','Т','Л','А','Н','А']

for i in permutations(a, 8):
    for j in range(len(i)-1):
        if i[j] != i[j+1]:
            s = True
        else:
            s = False
            break
    if s == True:
        print(i)
        counter += 1
        s = False
print(counter)