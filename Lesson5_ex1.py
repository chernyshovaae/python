with open("new_file_ex1.txt", "w", encoding='utf-8') as file_:
    get_line = ' '
    while get_line:
        get_line = input('Введите строку:\n')
        file_.write(f'{get_line}\n')
