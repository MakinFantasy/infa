# +1 +3 *2

def f(x,y):
    if x == y:
        return 1
    elif x > y or x == 12:
        return 0
    elif x < y:
        return f(x+1, y) + f(x+3, y) + f(x*2, y)

print(f(3, 8) * f(8, 21))  