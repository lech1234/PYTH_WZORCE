def f1():
    X = 'wartosc X'
    Y = 'wartosc Y'
    def f1_1():
        print(X)
        print(Y)
    return f1_1

nowa_f = f1()
# nowa_f()
print(nowa_f.__closure__[1].cell_contents)
