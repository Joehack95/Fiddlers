import numpy as np


class Dice:

    def __init__(self, n_sides):
        self.n_sides = n_sides

    def roll(self):
        return np.random.randint(1, self.n_sides)
