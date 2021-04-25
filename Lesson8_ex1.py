class Date:
    calendar_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_num(cls, getdate):
        dd, mm, yyyy = getdate.split('-')
        return cls(dd, mm, yyyy)

    @staticmethod
    def date_valid(valdd, valmm, valyear):
        try:
            valmm = int(valmm)
            valdd = int(valdd)
            valyear = int(valyear)
        except ValueError:
            return 'Неверый формат даты'
        else:
            if valmm in Date.calendar_dict.keys() \
                    and valdd in range(Date.calendar_dict[int(valmm)]) \
                    and valyear in range(1800, 3999):
                return 'Дата корректна'
            else:
                return 'Дата ведена некорректно'


objDate = Date.date_num(input('Введите дату формата "ДД-ММ-ГГГГ":\n'))
objDateValid = Date.date_valid(objDate.day, objDate.month, objDate.year)
print(objDateValid)
