""" файл "text_3.txt" использован из приложенных материалов """

with open("text_3.txt", "r", encoding='utf-8') as file_:
    list_ = [i.split() for i in file_.readlines()]
    list_salary = [float(j) for i in list_ for j in i[1::2]]
    list_min_salary = [float(j) for i in list_ for j in i[1::2] if float(j) < 20000.0]
    list_spec = [j for i in list_ for j in i[::2] if float(i[i.index(j) + 1]) < 20000.0]
    print(f'Сотрудники с окладом менее 20 тыс.:\n{list_spec}')
    print(f'Средняя величина дохода этих сотрудников:\n{round(sum(list_min_salary) / len(list_min_salary), 2)}')
    print(f'Средняя величина дохода всех сотрудников:\n{round(sum(list_salary) / len(list_salary), 2)}')
