any_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_list = [i for i in any_list if any_list.count(i) == 1]
print(f'Список уникальных элементов:\n{res_list}')
