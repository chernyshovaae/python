get_proc = int(input('Выручка:\n'))
get_cost = int(input('Издержка:\n'))
get_count = int(input('Количество сотрудников:\n'))
if get_proc > get_cost:
    r_prof = round((get_proc - get_cost) / get_proc * 100, 2)
    print(f'Рентабельность: {r_prof} %')
    print(f'Прибыль на 1 сотрудника: {round((get_proc - get_cost) / get_count)}')
else:
    print(f'Убыток {get_cost - get_proc}')
