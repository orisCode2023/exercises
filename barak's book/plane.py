import random


class Plane:


    def __init__(self , airport):
        self._x = airport[0]
        self._y = airport[1]

    def update_position(self):
        self._x += random.randint(-1 , 1)
        self._y += random.randint(-1 , 1)

    def get_position(self):
        return self._x, self._y

    def __str__(self):
        return "Plane position: {}".format(self.get_position())



