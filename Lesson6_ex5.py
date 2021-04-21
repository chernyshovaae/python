class Stationery:
    def __init__(self, nm):
        self.name = nm

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, name=''):
        super().__init__(name)

    def draw(self):
        print('Запись ручкой.')


class Pencil(Stationery):
    def __init__(self, name=''):
        super().__init__(name)

    def draw(self):
        print('Запись карандашом.')


class Handle(Stationery):
    def __init__(self, name=''):
        super().__init__(name)

    def draw(self):
        print('Запись маркером.')


get_Stationery = input('Введите канцелярский предмет(Pen, Pencil, Handle):\n')
objStationery = Stationery(get_Stationery)
objStationery.draw()

if get_Stationery == 'Pen':
    objPen = Pen()
    objPen.draw()
elif get_Stationery == 'Pencil':
    objPencil = Pencil()
    objPencil.draw()
elif get_Stationery == 'Handle':
    objHandle = Handle()
    objHandle.draw()
else:
    print('Канцелярия отсутствует')
