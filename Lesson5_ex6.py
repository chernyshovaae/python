""" файл "text_6.txt" использован из приложенных материалов """

dict_ = {}
with open("text_6.txt", "r", encoding='utf-8') as file_:
    for i in file_.readlines():
        list_n = [i for i in i.replace(':', '').replace('(', ' ').split() if i.isalpha() or i.isnumeric()]
        for j in range(len(list_n)):
            if list_n[j].isnumeric():
                list_n[j] = int(list_n[j])
        dict_[list_n[0]] = sum(list_n[1:])
print(dict_)
