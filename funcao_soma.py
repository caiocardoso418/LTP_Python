def imprime(s):
    print(s)
    print(id(s))


def soma(x, y):
    return (x+y)


def concaten(x, y):
    z = x + y
    return z


z = soma(6, 7)

a = "Caio"
b = "Peliz"
w = concaten(a, b)

imprime(w)
print(id(w))
imprime(z)
