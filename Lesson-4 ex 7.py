def f_factorial(num):
    for i in range(1, num):
        yield i


get_num = int(input('Введите число:\n'))
for i in f_factorial(get_num):
    get_num *= i
print(f'Факториал числа = {get_num}')
