alphabet_ = 'abcdefghijklmnopqrstuvwxyz'

""" Задача 6.1 - слово из маленьких латинских букв """


def int_func(get_word):
    for i in get_word:
        if i in alphabet_:
            check = True
        else:
            check = False
            break
    if not get_word.islower():
        check = False
    return get_word.title() if check else False


print(int_func(input('Введите слово, состоящее из маленьких латинских букв:\n')))

""" Задача 6.2 - строка из слов, разделенных пробелом """


def f_title(get_line):
    res_list = []
    for i in range(len(get_line)):
        if int_func(get_line[i]):
            res_list.append(int_func(get_line[i]))
    return ' '.join(res_list)


print(f_title(input('Введите строку из слов через пробел:\n').split()))
