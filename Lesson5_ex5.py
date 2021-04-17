list_num = '123456'
with open("new_file_ex5.txt", "w", encoding='utf-8') as new_file_:
    new_file_.write(' '.join(list_num))

with open("new_file_ex5.txt", "r", encoding='utf-8') as file_:
    list_num_new = [int(j) for i in file_.read() for j in i if j.isnumeric()]
    print(f'Сумма чисел в файле = {sum(list_num_new)}')
