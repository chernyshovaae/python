class CheckTypeNum(Exception):
    def __init__(self, message):
        self.message = message


def f_sum():
    sum_ = 0
    get_list = []
    while True:
        get_line = input('Введите список чисел через пробел:\n')
        get_list = get_line.split()

        if 'q' in get_list:
            get_list.pop(get_list.index('q'))
            try:
                if not get_line.replace(' ', '').isnumeric() and not 'q' in get_line:
                    raise CheckTypeNum('Ошибка - введены нечисленные значения!')
            except CheckTypeNum as msg:
                print(msg, '\nДля выхода команда q\n', sum_)
            else:
                sum_ += sum([int(i) for i in get_list])
                return f'{sum([int(i) for i in get_list])}({sum_})'
        else:
            try:
                if not get_line.replace(' ', '').isnumeric():
                    raise CheckTypeNum('Ошибка - введены нечисленные значения!')
            except CheckTypeNum as msg:
                print(msg, '\nДля выхода команда q\n', sum_)
            else:
                sum_ += sum([int(i) for i in get_list])
                print(f'{sum([int(i) for i in get_list])}({sum_})')


print(f_sum())
