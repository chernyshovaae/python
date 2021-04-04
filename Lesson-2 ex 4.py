get_str = input('Введите предложение:\n')
get_str = get_str.split()
for k, v in enumerate(get_str, start=1):
    print(k, v.replace(v[10:], ''))
