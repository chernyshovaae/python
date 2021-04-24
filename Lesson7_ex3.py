class OrganicCell:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return str(self.count)

    """ сложение """

    def __add__(self, other):
        return OrganicCell(self.count + other.count)

    """ вычитание """

    def __sub__(self, other):
        res = self.count - other.count
        return OrganicCell(res) if res > 0 else f'Вычитаемое значение превышает количество ячеек'

    """ умножение """

    def __mul__(self, other):
        return OrganicCell(self.count * other.count)

    """ деление """

    def __truediv__(self, other):
        try:
            return OrganicCell(self.count // other.count)
        except ZeroDivisionError:
            return f'Не делится на нулевое значение'

    def make_order(self, series):
        res = '\n'.join(['*' * series for i in range(self.count // series)])
        res_rem = '*' * (self.count % series)
        return f'{res}\n{res_rem}'


objCellOne = OrganicCell(int(input('Введите количество ячеек для первой клетки:\n')))
objCellTwo = OrganicCell(int(input('Введите количество ячеек для второй клетки:\n')))
series1 = int(input('Введите количество рядов для первой клетки:\n'))
series2 = int(input('Введите количество рядов для второй клетки:\n'))
print(f'Результат суммы клеток: {objCellOne + objCellTwo}')
print(f'Результат вычитания клеток: {objCellOne - objCellTwo}')
print(f'Результат умножения клеток: {objCellOne * objCellTwo}')
print(f'Результат деления клеток: {objCellOne / objCellTwo}')
print(f'Клетка № 1:\n{objCellOne.make_order(series1)}')
print(f'Клетка № 2:\n{objCellTwo.make_order(series2)}')
