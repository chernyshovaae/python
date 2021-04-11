""" Способ I """


def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return 'Неверный тип данных'
    if x <= 0 or y >= 0:
        return 'x должен быть положительным и y отрицательным'
    else:
        return round(x ** y, 4)


""" Способ II """


def my_func_hard(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return 'Неверный тип данных'
    if x <= 0 or y >= 0:
        return 'x должен быть положительным и y отрицательным'
    else:
        res = 1
        for i in range(abs(y)):
            res *= x
        return round(1 / res, 4)


print('Введите положительное действительное число x и целое отрицательное y:\n')
get_x = input('x:\n')
get_y = input('y:\n')
print(f'Способ I : {my_func(get_x, get_y)}')
print(f'Способ II: {my_func_hard(get_x, get_y)}')
