"""  Способ I """


def t_func(a, b):
    try:
        return f'Аргумент 1 / Аргумент 2 = {int(a) / int(b)}'
    except ZeroDivisionError:
        return 'Ошибка деления на 0'
    except ValueError:
        return 'Введено нечисловое значение'


""" 
    Способ II 
"""


def s_func(a, b):
    try:
        return f'Аргумент 1 / Аргумент 2 = {int(a) / int(b)}'
    except (ZeroDivisionError, ValueError) as err:
        return 'Ошибка деления на 0' if err == 'division by zero' else 'Введено нечисловое значение'


print('Введите два аргумента:\n')
print(t_func(input('Аргумент 1:\n'), input('Аргумент 2:\n')))
print('Способ II\n')
print(s_func(input('Аргумент 1:\n'), input('Аргумент 2:\n')))
