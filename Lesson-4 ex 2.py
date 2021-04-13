from random import randint

any_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_tbtb = [any_list[i] for i in range(1, len(any_list)) if any_list[i] > any_list[i - 1]]
print(f'the bigger, the better:\n{list_tbtb}')

gen_list = [randint(1, 50) for i in range(5)]
print(f'generation list:\n{gen_list}')
gen_list_tbtb = [gen_list[i] for i in range(1, len(gen_list)) if gen_list[i] > gen_list[i - 1]]
print(f'the bigger, the better (generation):\n{gen_list_tbtb}')
