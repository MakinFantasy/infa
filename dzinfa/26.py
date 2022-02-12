t = open('26-j1.txt')
n = int(t.readline())
arr = t.readlines()
print(n)
count = 0
for i in range(n):
    arr[i] = arr[i].replace('\n', '')
print(len(arr))
print(arr)
for i in range(1, 51):
    if (arr.count(str(i)) > arr.count(str(100-i))):
        count += arr.count(str(100-i))
    elif( arr.count(str(i)) < arr.count(str(100-i)) ):
        count += arr.count(str(i))
    else:
        count += arr.count(str(i))//2
print(count)