class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка движения')

    def turn(self, direction):
        if direction == 'go':
            self.go()
        elif direction == 'stop':
            self.stop()
        else:
            print(f'Поворот {direction}')

    def show_speed(self):
        print(f'Автомобиль: {self.color} {self.name}\nСкорость: {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости!')
        else:
            print(f'Городской автомобиль: {self.color} {self.name}\nСкорость: {self.speed} км/ч')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости!')
        else:
            print(f'Рабочий автомобиль: {self.color} {self.name}\nСкорость: {self.speed} км/ч')


class SportCar(Car):

    def show_speed(self):
        print(f'Спортивный автомобиль: {self.color} {self.name}\nСкорость: {self.speed} км/ч')


class is_police(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Полицейский автомобиль: {self.color} {self.name}\nСкорость: {self.speed} км/ч')


print('Введите параметры автомобиля:')
try:
    get_speed = int(input('Скорость:\n'))
except ValueError:
    print('Введено нечисленное значение')
get_color = input('Цвет:\n')
get_name = input('Название:\n')
get_type = input('Тип (TownCar, SportCar, WorkCar, PoliceCar):\n')
get_turn = input('Действие go, stop или поворот (налево, направо):\n')

check_type = ''
if get_type == 'TownCar':
    objCar = TownCar(get_speed, get_color, get_name)
elif get_type == 'SportCar':
    objCar = SportCar(get_speed, get_color, get_name)
elif get_type == 'WorkCar':
    objCar = WorkCar(get_speed, get_color, get_name)
elif get_type == 'PoliceCar':
    objCar = is_police(get_speed, get_color, get_name)
else:
    check_type = 'not'
    print('Данного типа нет в базе')

if not check_type:
    objCar.show_speed()
    objCar.turn(get_turn)
