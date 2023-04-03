def generator1(p1, p2):
    print('Start generatora wywołanego z ', p1, p2)
    print('w1')
    yield 'w1'
    print('w2')
    yield 'w2'
    print('w3')
    yield 'w3'
    print('koniec generatora')
    return None


# g = generator1(1, 2)
# print(g)
# i = g.__iter__()
# print(i)
# print(i.__next__())
# print('-----')
# print(i.__next__())
# print('-----')
# print(i.__next__())
# print('-----')
# print(i.__next__())

for e in generator1(3, 4):
    print('konsumuję', e)
