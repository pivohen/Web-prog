import copy #копирование переменной


def add(a):
    c = copy.copy(a)
    c.append(4)
    print(
        id(c)
    )

    return sum(c)



b = [1, 2, 3]

print(
    id(b)
)

print(b)

print (
    add(b)
)

print(b)