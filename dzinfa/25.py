def delit(a):
	res = []
	i = 1
	while i * i < a + 1:
		if a % i == 0:
			res.append(i)
			if i != a // i:
				res.append(a // i)
		i += 1
	return sorted(res)


def fun(m, n):
	dres = []
	for num in range(m, n + 1):
		frac = delit(num)
		dres.append((len(frac), -num, frac[-2:]))
	dres.sort()
	print(-dres[-1][1], ' содержит ', dres[-1][0], ' делителей ')
	print('два его максимальных делителя ', dres[-1][2])


fun(394441, 394505)