from random import randint

def gen_random(n, s, f):
    for x in range(n):
        yield randint(s, f)