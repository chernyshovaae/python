dict_season = \
    {'Зима': [12, 1, 2]
        , 'Весна': [3, 4, 5]
        , 'Лето': [6, 7, 8]
        , 'Осень': [9, 10, 11]
     }
get_num = input('Введите номер месяца от 1 до 12:\n')
if not get_num.isdigit():
    print('Введено нечисленное значение')
else:
    get_num = int(get_num)
    if int(get_num) < 1 or get_num > 12:
        print('Введено значение за пределами указанного диапазона')
    else:
        for k, v in dict_season.items():
            if get_num in v:
                print(f'Введенный номер месяца относится ко времени года:\n{k}')
                break
