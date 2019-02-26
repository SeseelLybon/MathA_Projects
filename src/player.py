
from charter import Chart as charter_chart
from numpy import random

class Player:

    def __init__(self, name):
        self.chart = charter_chart()
        self.name = name
        self.done = False
        self.num_throws = 0
        self.throw = list()

    def isDone(self) -> bool:
        return self.done

    def new_throw(self):
        self.num_throws = 0
        self.throw = self.gen_throws()

    def rethrow(self, locked_dice):
        for i in range(0,4):
            if not locked_dice[i]:
                self.throw[i] = random.randint(1,6)

    @staticmethod
    def gen_throws() -> list:
        return list(random.randint(1, 6, 5))
