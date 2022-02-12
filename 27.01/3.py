j = 1635
for i in range(1000000000, 10000000000):
	x = i
	n = j
	while (x+n)//1000 < 465283:
		x = x - 2
		n = n + 5
	if n//1000==956:
		print(i)
		break

## 191200
