from functools import reduce

list_ = reduce(lambda el1, el2: el1 * el2, [i for i in range(100, 1001, 2)])
print(f'Список четных чисел от 100 до 1000:\n{[i for i in range(100, 1001, 2)]}')
print(f'Произведение элементов списка:\n{list_}')
