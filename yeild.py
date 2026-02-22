def f():
    return [43, 65, 32]

def genf():
    s = 7
    for i in [43, 65, 32]:
        yield i
        print(s)
        s = s*10 + 7

s = genf()
print(next(s))
print(next(s))
print(next(s))

g = genf()
# print(next(g))
# print(next(g))

def list_numbers():
    yield from [13, 14]

gen = list_numbers()

# print(next(gen))
# print(next(gen))


# Задания

# 1
def even_numbers(n):
    if n % 2 == 0:
        n += 1

    while True:
        yield n
        n += 2

gen1 = even_numbers(10)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

# 2

def geom_progression(start, step):
    while True:
        yield start
        start *= step

gen2 = geom_progression(2, 3)

# print(next(gen2))
# print(next(gen2))
# print(next(gen2))

# 3

def word_filter(text):
    if text.istitile == True:
        yield text.split(1)
    else:
        raise SyntaxError ('Error')


# 4

def count_up(start, step):
    while True:
        yield start
        step = start = 1

print(count_up(4, 3))



