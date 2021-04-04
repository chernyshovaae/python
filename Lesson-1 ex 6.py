get_first_km = int(input('Введите результат пробежки (км.) в первый день:\n'))
get_end_km = int(input('Введите целевой результат пробежки (км.):\n'))
count_day = 1
while get_first_km < get_end_km:
    get_first_km += (get_first_km * 0.1)
    count_day += 1
    # print(get_first_km)
print(f'На {count_day} день спортсмен достиг результата — не менее {get_end_km} км')
