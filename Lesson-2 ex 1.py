# проверка типов данных элементов списка
any_list = [6, 2.13, 'banana', 0b0101, [2, 'joy'], False, bin(12), 0]
for i in any_list:
    print(f'Элемент: {str(i):<10}', f'Тип: {type(i)}')
