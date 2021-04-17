""" файл "file_ex2.txt" создан вручную """

with open("file_ex2.txt", "r", encoding='utf-8') as file_:
    print(f'Количество строк: {len(file_.readlines())}')
    file_.seek(0)
    for i, j in enumerate(file_.readlines(), start=1):
        print(f'Строка {i}: {len(j.split())} слов')
