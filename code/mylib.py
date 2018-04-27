# -*- coding: utf-8 -*-
from functools import reduce


def product(x, *y):
    sum = x
    for n in y:
        sum *= n
    return sum


def move(n, a, b, c):
    if n == 1:
        print(a, '----->', c)
    else:
        move((n - 1), a, c, b)
        move(1, a, b, c)
        move((n - 1), b, a, c)


def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])
    return s


def findMinAndMax(L):
    x = L[0]
    y = L[0]
    for i in L:

        if i < x:
            x = i
        if i > y:
            y = i
    return (x, y)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


def triangles():
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)
        if len(L) > 10:
            break


def add(x, y, f):
    return f(x) + f(y)


def normalize(name):
    return name[0].upper() + name[1:].lower()


def prod(L):
    def multp(x, y):
        return x * y

    return reduce(multp, L)


def str2float(s):
    def multp(x, y):
        return x * 10 + y

    n = s.index('.')
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    return reduce(multp,s1) + reduce(multp,s2)/10**len(s2)
def _odd_iter():
    n = 1
    while True:
        n+=2
        yield n
def _not_divisible(n):
    return lambda x: x%n > 0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
def is_palindrome():
