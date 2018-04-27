from code import mylib


for n in mylib.primes():
    if n < 100:
        print(n)
    else:
        break