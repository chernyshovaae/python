rating_list = [11, 9, 4, 4, 2]
el_ = input('Введите новый элемент в список рейтинга в виде числа:\n')
if not el_.isdigit():
    print('Введено нечисленное значение')
else:
    el_ = int(el_)
    if not el_ in rating_list:
        if min(rating_list) > el_:
            rating_list.append(el_)
        else:
            for k, v in enumerate(rating_list):
                if el_ > v:
                    rating_list.insert(k, el_)
                    break
    else:
        step_count_ = rating_list.count(el_)
        while step_count_ > 0:
            for k, v in enumerate(rating_list):
                if el_ == v:
                    j = k
                    step_count_ -= 1
        rating_list.insert(j, el_)
    print(rating_list)
