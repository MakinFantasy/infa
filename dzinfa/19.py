from functools import lru_cache
# +2, *2


def moves(h):
    a, b = h
    return (a+2, b), (a*2, b), (a, b+2), (a, b*2)


@lru_cache(None)
def f(s):
    if sum(s) >= 82:
        return 'END'
    elif any(f(x) == 'END' for x in moves(s)):
        return 'П1'
    elif any(f(x) == 'П1' for x in moves(s)):
        return 'В1'


for i in range(1, 73):
    h = 9,i
    print(i, f(h))
# Ответ 19