# +1 *3

def f(n):
	if n > 49:
		return 0
	elif n == 49:
		return 1
	return f(n + 1) + f(n*3)


print(f(5))