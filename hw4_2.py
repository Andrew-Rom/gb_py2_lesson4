"""
HW 4-2
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где
ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


def get_dic_from_kwargs(**kwargs):
    res = dict()
    for key, value in kwargs.items():
        if type(value) is not hash:
            value = str(value)
        res.update({value: key})
    return res


print(get_dic_from_kwargs(a=1, b=2, c=3, lst=[1, 2, 3], tupl=(1, 2), dic={1: 2, 0:'p'}))
