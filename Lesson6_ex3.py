class Worker:
    def __init__(self, n, sn, pos, inc):
        self.name = n
        self.surname = sn
        self.position = pos
        self._income = inc


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
        self.get_full_name = ' '.join([name, surname])
        self.get_total_income = sum(list(self._income.values()))

    def info(self):
        return f'{self.position}: {self.get_full_name}\nДоход с учетом премии: {self.get_total_income}'


print('Введите данные сотрудника:')
objPos = Position(input('Имя:\n'), input('Фамилия:\n'), input('Должность:\n'), \
                  {'wage': int(input('Оклад:\n')), 'bonus': int(input('Премия:\n'))})
print(objPos.info())
