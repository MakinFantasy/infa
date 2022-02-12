# +1 +2 *2 [31]
from functools import lru_cache


def moves(h):
    return [h+1, h+2, h*2]


@lru_cache(None)
def f(s):
    if s >= 31:
        return "END"
    elif any(f(i) == "END" for i in moves(s)):
        return "P1"
    elif all(f(i) == "P1" for i in moves(s)):
        return "V1"



for i in range(1,30):
    print(i,  f(i))