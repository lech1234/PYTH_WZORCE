import functools
import logging

logging.basicConfig(filename='moj.log',
                    filemode='wt',
                    encoding='utf8',
                    level=logging.INFO)


class loguj():
    """
    Dokumentacja dekoratora

    UWAGA: Wywoływać zawsze z nawiasami
    """

    def __init__(self, ok_level=logging.DEBUG, error_level=logging.ERROR):
        self._ok_level = ok_level
        self._error_level = error_level

    def __call__(self, f):

        @functools.wraps(f)
        def f_nowa(*args, **kwargs):
            lgr = logging.getLogger(__name__)
            lgr.log(self._ok_level, f'Wywołanie {f.__qualname__}({args=}, {kwargs=})')
            try:
                r = f(*args, **kwargs)
            except BaseException as e:
                lgr.log(self._error_level, f'Wywołanie {f.__qualname__}({args=}, {kwargs=}) wyrzuciło błąd {e}.')
                raise
            lgr.log(self._ok_level, f'Wywołanie {f.__qualname__}({args=}, {kwargs=}) -> {r}')
            return r

        return f_nowa


class A:
    @loguj(ok_level=logging.DEBUG, error_level=logging.ERROR)
    def m1(self, x, y):
        print('f1', x, y)
        return x / y


a = A()
a.m1(3, 9)
a.m1(3, 0)
