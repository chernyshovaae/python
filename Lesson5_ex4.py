""" файл "text_4.txt" использован из приложенных материалов """

num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("text_4.txt", "r", encoding='utf-8') as file_:
    list_ = [i.split(' ') for i in file_]
    list_new = [num_dict.get(j) if j in num_dict else j for i in list_ for j in i]

with open("new_text_4.txt", "w", encoding='utf-8') as new_file_:
    for i in range(0, len(list_new), 3):
        new_file_.writelines(' '.join(list_new[i:i + 3]))
