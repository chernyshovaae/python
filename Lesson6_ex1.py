import time
from datetime import datetime


class TrafficLight:
    __color = ['red', 'yellow ', 'green']
    """ таймер на 30 секунд """
    __cur_time = datetime.fromtimestamp(time.time())
    __count_time = datetime.fromtimestamp(float(time.time()) + 30)

    def running(self):
        while self.__cur_time < self.__count_time:
            print(f'\033[31m {self.__color[0]}')
            time.sleep(7)
            print(f'\033[33m {self.__color[1]}')
            time.sleep(2)
            print(f'\033[32m {self.__color[2]}')
            time.sleep(5)
            self.__cur_time = datetime.fromtimestamp(time.time())
        print('\033[37m Stop')


objTL = TrafficLight()
objTL.running()
