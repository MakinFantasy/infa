from pprint import pprint


def f(n):
    if n <= 3:
        return n
    elif n%2 == 0:
        return n + 3 + f(n-1)
    elif n%2 != 0:
        return n*n + f(n-2)


if __name__ == '__main__':
    counter = 0
    for i in range(1,1001):
        if f(i) % 7 == 0:
            counter += 1
pprint(counter)