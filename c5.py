import time


# class A:
#     def __enter__(self):
#         print('__enter__')
#         return self
#
#     def __exit__(self, err_cls, err, tb):
#         print(err_cls, err, tb)
#
#
# with A() as a:
#     print('ciało with', a)
#     print('wychodzę')
#     # x = 9/0
#
# print('wyszedłem')

# Napisać menedżera kontekstu, który będzie mierzył czas wykonania kodu pod with


class Stoperek:
    __slots__ = ['nazwa',
                 'start',
                 'koniec']

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        # start
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.koniec = time.perf_counter()

    def __repr__(self):
        return f'{self.nazwa}: {self.koniec - self.start:.2f}'

    # def __str__(self):
    #     return f'S {self.nazwa}: {self.koniec - self.start:.2f}'


tmp = Stoperek('100_000 insertow')

with tmp as s:
    x = []
    for i in range(100_000):
        x.insert(0, i)

print([s])
