from random import randint
from time import sleep

class Simulator:
    def __init__(self):
        pass

    def set_number(self, number: int):
        if number < 0:
            raise ValueError ("no negative number")
        else:
            self.number = number
    def send_data(self) -> list:
        return [randint(1, 100) for x in range(self.number)]

    def print_data(self):
        while True:
            sleep(1)
            print(self.send_data())

    def print_list_data(self, data: list):
        if (type(data) != list) & (type(data) != tuple):
            raise TypeError ("data must be list type")
        return data[0]







sim = Simulator()
print(sim.print_list_data(5))

    