from functools import lru_cache
# +2, *2
def moves(h):
    a, b = h
    return (a+2, b), (a, b+2), (a*2, b), (a, b*2)


@lru_cache(None)
def f(h):
    if sum(h) >= 82:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return 'П1'
    elif all(f(x) == 'П1' for x in moves(h)):
        return 'В1'
    elif any(f(x) == 'В1' for x in moves(h)):
        return 'П2'
    elif all(f(x) == 'П2' or f(x) == 'П1' for x in moves(h)):
        return 'В2'

if __name__ == "__main__":
    for i in range(1, 100):
        h = 9,i
        print(i, f(h))

# Ответ 29, 33