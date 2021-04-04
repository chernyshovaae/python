get_list = input('Введите список элементов через пробел:\n')
get_list = list(get_list.split())
# способ работы с копией списка
copy_list = get_list.copy()
print(f'Исходный список:\n{copy_list}')
for k, j in enumerate(copy_list):
    if k % 2:
        get_list[k] = copy_list[k - 1]
        get_list[k - 1] = copy_list[k]
print(f'Список с обменом соседей - способ I:\n{get_list}')

# способ без использования копии; используется шаг
new_list = copy_list.copy()
list_odd = new_list[::2]
list_even = new_list[1::2]
step_f = 0
step_s = 1
for i in range(len(list_even)):
    if step_f <= len(new_list) - 1:
        new_list[step_f] = list_even[i]
        step_f += 2
for i in range(len(list_odd)):
    if step_s <= len(new_list) - 1:
        new_list[step_s] = list_odd[i]
        step_s += 2
print(f'Список с обменом соседей - способ II:\n{new_list}')
