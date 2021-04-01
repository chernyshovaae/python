get_num = int(input('Введите число:\n'))
# print(max(str(get_num)))
len_num = len(str(get_num))
res_num = 0
while len_num > 0:
    if res_num < get_num % 10:
        res_num = get_num % 10
    get_num //= 10
    len_num -= 1
print(res_num)
