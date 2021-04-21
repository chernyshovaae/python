class Road:
    __weight = 25
    __depth = 5

    def __init__(self, l, w):
        self._length = l
        self._width = w


    def all_weight(self):
        try:
            self._length = int(self._length)
            self._width = int(self._width)
        except ValueError:
            return 'Введены нечисленные данные'
        res = (self._length * self._width * self.__weight * self.__depth) / 1000
        return f'Масса асфальта для дорожного полотна = {res} т.'


objRoad = Road(input('Введите длину дорожного полотна(м):\n'), input('Введите ширину дорожного полотна(м):\n'))
print(objRoad.all_weight())
