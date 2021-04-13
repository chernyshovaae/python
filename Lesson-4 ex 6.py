from itertools import count, cycle

""" Задание 6.а - итератор, генерирующий целые числа, начиная с указанного """

for i in count(3, 1.1):
    if i > 10:
        break
    else:
        print(i)

""" Задание 6.б - итератор, повторяющий элементы некоторого списка, определенного заранее """

count_ = 0
any_list = [12, 'heap', 23.401, ['a', 1]]
for i in cycle(any_list):
    if count_ > 10:
        break
    print(i)
    count_ += 1
