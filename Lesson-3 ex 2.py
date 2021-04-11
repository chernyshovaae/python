t_list = ['Имя:', 'Фамилия:', 'Дата рождения:', 'Город:', 'E-mail:', 'Телефон:']
s_list = []


def func_(list_arg, list_val):
    for i in range(len(list_arg)):
        s_list.append(list_arg[i])
        s_list.append(list_val[i])
    return ' '.join(s_list)


print(func_(list_arg=t_list, list_val=[input(f'{i}') for i in t_list]))

""" Не именованные аргументы
def func_(*args):
    return ' '.join(list(*args))
print(func_([input(f'{i}') for i in t_list]))
"""
