from functools import lru_cache
def moves(x):
    a,b = x
    return [(a + 1, b), (a * 2, b), (a, b + 1), (a, b * 3)]
@lru_cache(None)
def f(s):
    if (sum(s) >= 84):
        return "END"
    elif (any(f(i) == "END" for i in moves(s))):
        return "P1"
    elif (all(f(i) == "P1" for i in moves(s))):
        return "V1"
    elif (any(f(i) == "V1" for i in moves(s))):
        return "P2"
    elif (all(f(i) == "P2" or f(i) == "P1"  for i in moves(s))):
        return "V2"
for i in range(1, 67):
    y = 16, i
    print(i, f(y))