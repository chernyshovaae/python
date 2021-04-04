# фиксированный список кортежей: номер товара, словарь параметров товара
any_list = \
    [
        (1, {'Название': 'Монитор', 'Цена': '15000', 'Количество': '10', 'СИ': 'шт.'}),
        (2, {'Название': 'Компьютер', 'Цена': '50000', 'Количество': '5', 'СИ': 'шт.'}),
        (3, {'Название': 'Клавиатура', 'Цена': '4000', 'Количество': '10', 'СИ': 'шт.'})
    ]


# Аналитика
def def_analyst():
    my_dict = {}
    for i, j in enumerate(any_list):  # индекс, кортеж
        for n, m in enumerate(any_list[i][1]):  # индекс эл-та кортежа, ключ словаря в кортеже
            if not my_dict.get(m):
                my_dict[m] = []
            my_dict[m].append(dict(any_list[i][1])[m])
    my_dict['СИ'] = list(set(my_dict['СИ']))
    return my_dict


# Добавить товар
def def_insert_good():
    print('Введите данные о товаре.\n')
    get_name = input('Название товара:\n')
    get_price = input('Цена товара:\n')
    get_num = input('Количество товара:\n')
    get_unit = input('Единица товара:\n')
    my_tuple = (len(any_list) + 1, {'Название': get_name, 'Цена': get_price, 'Количество': get_num, 'СИ': get_unit})
    any_list.append(my_tuple)


# Меню
get_command = input('Введите команду (список всех команд - help):\n')
if get_command == 'help':
    print('1 - добавить товар; 2 - вывести аналитику; 3 - добавить товар и вывести аналитику')
elif get_command == '1':
    def_insert_good()
    print(any_list)
elif get_command == '2':
    print(def_analyst())
elif get_command == '3':
    def_insert_good()
    print(def_analyst())
else:
    print('Введена неверная команда')
