
from charter import Chart as charter_chart
from random import randint

class Player:

    def __init__(self, name):
        self.chart = charter_chart()
        self.name = name
        self.done = False
        self.num_throws = 0
        self.throw = list()

    def isDone(self):
        return self.done

    def new_throw(self):
        self.num_throws = 0
        self.throw = self.gen_throws()

    def rethrow(self, locked_dice):
        if self.num_throws <= 3:
            self.num_throws += 3
            for i in locked_dice:
                if i == 0:
                    self.throw[0] = randint(1, 6)
        else:
            print("Player can't throw more")

    @staticmethod
    def gen_throws():
        return [randint(1, 6),
                randint(1, 6),
                randint(1, 6),
                randint(1, 6),
                randint(1, 6)
                ]