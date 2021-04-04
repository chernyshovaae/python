main_msg = 'Профиль пользователя. Введите данные.\n'
print(main_msg)
user_name = input('Имя:\n')
user_age = int(input('Возраст:\n'))
user_city = input('Место жительства:\n')
user_job = int(input('Стаж:\n'))
print(f'Данные пользователя {user_name}. Возраст: {user_age} лет. Место жительства: {user_city}. Стаж: {user_job} лет.')
