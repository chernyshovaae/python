class CheckDivZero(Exception):
    def __init__(self, message):
        self.message = message


get_dividend = input('Введите делимое:\n')
get_divider = input('Введите делитель:\n')
try:
    get_dividend = int(get_dividend)
    get_divider = int(get_divider)
    if get_divider == 0:
        raise CheckDivZero('Ошибка - попытка деления на 0!')
except (ValueError, CheckDivZero) as msg:
    print(msg)
else:
    print(f'{get_dividend} / {get_divider} = {round(get_dividend / get_divider, 4)}')
