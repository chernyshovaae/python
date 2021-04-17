""" файл "text_7.txt" использован из приложенных материалов """
import json

dict_firms = {}
dict_avg = {}
with open("text_7.txt", "r", encoding='utf-8') as file_:
    for i in file_.readlines():
        list_ = i.split()
        for j in enumerate(list_):
            dict_firms[list_[0]] = int(list_[2]) - int(list_[3])
list_sum = [int(i) for i in dict_firms.values() if i > 0]
dict_avg['Средняя прибыль'] = sum(list_sum) / len(list_sum)

with open("new_text_7.json", "w", encoding='utf-8') as file_js:
    json.dump([dict_firms, dict_avg], file_js, ensure_ascii=False, indent=4)
