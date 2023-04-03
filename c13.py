from typing import Any


def auto_property(cls_name:dict[str, Any], cls_inh, cls_dict):
    new_d = {}
    for atr_name, atr_val in cls_dict.items():
        # TU !!!!
        if atr_name.startswith('_set'):
            public_name = atr_name.removeprefix('_set_')
            new_d[public_name] = property(fget=cls_dict[f'_get_{public_name}'],
                             fset=atr_val)
        new_d[atr_name] = atr_val
    return type(cls_name, cls_inh, new_d)


class A(metaclass=auto_property):
    def _set_atr1(self, w):
        self._atr1 = w

    def _get_atr1(self):
        return self._atr1

    # to będzie automatycznie dodane do klasy przez metaklasę
    # atr1 = property(fget=_get_atr1, fset=_set_atr1)

a = A()
a.atr1 = 22
print(a.atr1)