from functools import lru_cache

# Все возможные ходы в куче
def moves(h):
    return h+1, h+2, h*3


# ОБЯЗАТЕЛЬНЫЙ ДЕКОРАТОР ФУНКЦИИ
@lru_cache(None)
def f(h):
    if (h > 54):
        return "END"
    elif any(f(x) == 'END' for x in moves(h)):
        return "П1"
    elif all(f(x) == 'П1' for x in moves(h)):
        return 'В1'
    elif any(f(x) == 'В1' for x in moves(h)):
        return 'П2'
    elif all(f(x) == 'П2' or f(x) == 'П1' for x in moves(h)):
        return 'В2'

if __name__ == '__main__':
    for i in range(1, 100):
        print(i, f(i))

# Проверка условий в фунции f, вызов обычным циклом рпоходясь по множеству решений.
