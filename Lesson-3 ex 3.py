def my_func(a, b, c):
    list = [a, b, c]
    max1 = list.pop(list.index(max(list)))
    max2 = list.pop(list.index(max(list)))
    return f'Сумма максимальных аргументов {max1} и {max2} = {sum([max1, max2])}'


try:
    print(my_func(int(input('Аргумент 1:\n')), int(input('Аргумент 2:\n')), int(input('Аргумент 3:\n'))))
except ValueError:
    print('Введите числа')
