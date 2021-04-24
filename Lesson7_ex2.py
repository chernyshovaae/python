from abc import abstractmethod, ABC

""" abstractmethod - объявленный, но не реализованный метод; необх. переопределять для каждого подкласса """


class Clothes(ABC):
    def __init__(self, ind):
        self.ind = ind

    @property
    @abstractmethod
    def calc(self):
        return 0

    def __add__(self, other):
        return self.calc + other.calc


class Сoat(Clothes):
    @property
    def calc(self):
        return round(self.ind / 6.5 + 0.5)


class Suit(Clothes):
    @property
    def calc(self):
        return round(self.ind * 2 + 0.3)


objCoat = Сoat(int(input('Введите размер:\n')))
objSuit = Suit(int(input('Введите рост: \n')))
print(f'Расход ткани на пальто: {objCoat.calc}')
print(f'Расход ткани на костюм: {objSuit.calc}')
print(f'Общий расход ткани: {objCoat + objSuit}')
