import math
import random

from enum import Enum
from enum import auto


class States(Enum):
    yatzee = auto
    full_house = auto
    short_straight = auto
    long_straight = auto
    three_total = auto
    four_total = auto
    chance = auto
    ones = auto
    twos = auto
    threes = auto
    fours = auto
    fives = auto
    sixes = auto


def gen_throws():
    return [random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6)
            ]


throws = gen_throws()

print(throws)


def check_throw(throw):
    results = list()
    if throw[0]\
        == throw[1] == throw[2]\
        == throw[3] == throw[4] == throw[5]:

        results.append(States.yatzee)
        if throw[0] == 1:
            results.append(States.ones)
        elif throw[0] == 2:
            results.append(States.twos)
        elif throw[0] == 3:
            results.append(States.threes)
        elif throw[0] == 4:
            results.append(States.fours)
        elif throw[0] == 5:
            results.append(States.fives)
        elif throw[0] == 6:
            results.append(States.sixes)

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw or \
        2 in throw and 3 in throw and 4 in throw and 5 in throw or \
        3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append(States.short_straight)

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw and 5 in throw or \
        2 in throw and 3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append(States.long_straight)