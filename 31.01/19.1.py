from functools import lru_cache

def moves(h):
    return h+2, h*2

def f(h):
    if h > 25:
        return 'end'
    elif any(f(x) == 'end' for x in moves(h)):
