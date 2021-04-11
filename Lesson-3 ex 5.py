def f_sum():
    sum_ = 0
    get_list = []
    while True:
        get_list = input('Введите список чисел через пробел:\n').split()
        if 'q' in get_list:
            get_list.pop(get_list.index('q'))
            sum_ += sum([int(i) for i in get_list])
            return f'{sum([int(i) for i in get_list])}({sum_})'
        else:
            try:
                sum_ += sum([int(i) for i in get_list])
                print(f'{sum([int(i) for i in get_list])}({sum_})')
            except ValueError:
                print('Для выхода команда q\n', sum_)


print(f_sum())
