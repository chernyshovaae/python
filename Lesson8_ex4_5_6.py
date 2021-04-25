class CheckTypeNum(Exception):
    def __init__(self, message):
        self.message = message


from abc import ABC, abstractmethod


class Warehouse:
    __data_base = {'Unit Tech':
                       {},
                   'recycling':
                       {},
                   'repair':
                       {},
                   'non-core':
                       {}
                   }

    def __init__(self, goods):
        self.goods = goods

    @staticmethod
    def valid(num=0, line=''):
        try:
            if not type(num) == int:
                raise CheckTypeNum('Ошибка - введены нечисленные значения!')
        except CheckTypeNum as msg:
            return msg
        else:
            return 'success'

    def get_goods(self, kind, num):
        if self.valid(num=num) == 'success' and self.valid(line=kind) == 'success':
            if kind in ['принтер', 'сканер', 'МФУ']:
                self.__data_base['Unit Tech'][self.goods] = num
            else:
                self.__data_base['non-core'][self.goods] = num
            return self.__data_base
        else:
            return self.valid(num=num) if self.valid(num=num) != 'success' else self.valid(line=kind)

    def unit_move(self, unit):
        ind = [i for i in self.__data_base.keys() if self.goods in self.__data_base[i]]
        self.__data_base[unit] = {self.goods: self.__data_base[ind[0]][self.goods]}
        self.__data_base[ind[0]].pop(self.goods)
        return self.__data_base


class Tech(Warehouse, ABC):
    def __init__(self, name, color=False):
        self.name = name
        self.color = color

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def speed_info(self, speed):
        pass


class Print(Tech):
    def __init__(self, name, color=False, laser=False):
        super().__init__(name, color)
        self.laser = laser

    @property
    def info(self):
        cartridge = 'цветной' if self.color else 'ч/б'
        type = 'Лазерный' if self.laser else 'Струйный'
        return f'{type} {cartridge} принтер {self.name}'

    @property
    def speed_info(self, speed):
        return f'Скорость печати: {self.speed} стр/мин'


class Scan(Tech):
    def __init__(self, name, color=False, tablet=False):
        super().__init__(name, color)
        self.tablet = tablet

    @property
    def info(self):
        cartridge = 'цветной' if self.color else 'ч/б'
        type = 'Планшетный' if self.tablet else 'Протяжной'
        return f'{type} {cartridge} сканер {self.name}'

    @property
    def speed_info(self, speed):
        return f'Скорость сканирования: {self.speed} стр/мин'


class Xerox(Tech):
    def __init__(self, name, color=False, laser=False, tablet=False):
        super().__init__(name, color)
        self.laser = laser
        self.tablet = tablet

    @property
    def info(self):
        cartridge = 'цветной' if self.color else 'ч/б'
        type1 = 'Лазерный' if self.laser else 'Струйный'
        type2 = 'Планшетный' if self.tablet else 'Протяжной'
        return f'{type1} {type2} {cartridge} МФУ {self.name}'

    @property
    def speed_info(self, speed):
        return f'Скорость сканирования и печати: {self.speed} стр/мин'


""" задание 4 """

print(Print('Brother HL1223WR').info)
print(Xerox('HP LaserJet Pro M428fdn', color=True, laser=True, tablet=True).info)

""" задание 5 """

objWarehouse = Warehouse('Brother HL1223WR')
print(objWarehouse.get_goods('принтер', 1))
objWarehouse = Warehouse('Fujitsu fi-7030')
print(objWarehouse.get_goods('сканер', 4))
objWarehouse = Warehouse('Brother HL1223WR')
print(objWarehouse.unit_move('repair'))

""" задание 6 """

objWarehouse = Warehouse('HP LaserJet Pro M428fdn')
print(objWarehouse.get_goods('МФУ', '7'))
