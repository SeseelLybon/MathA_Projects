import math
import random

from enum import Enum
from enum import auto as enum_auto


class States(Enum):
    yatzee = enum_auto()
    full_house = enum_auto()
    short_straight = enum_auto()
    long_straight = enum_auto()
    three_total = enum_auto()
    four_total = enum_auto()
    chance = enum_auto()
    ones = enum_auto()
    twos = enum_auto()
    threes = enum_auto()
    fours = enum_auto()
    fives = enum_auto()
    sixes = enum_auto()

states_names = {
    States.yatzee: "Yatzee",
    States.full_house:  "Full house",
    States.short_straight:  "short straight",
    States.long_straight:  "long straight",
    States.three_total:  "Threes total",
    States.four_total:  "Four_total",
    States.chance:  "Chance",
    States.ones:  "Ones",
    States.twos:  "Twos",
    States.threes:  "Threes",
    States.fours:  "Fours",
    States.fives:  "Fives",
    States.sixes:  "Sixes"
}

def temp_repr(throw_states):
    for state, score in throw_states:
        print("\t",states_names[state], " ", score)
    return

def xes_score(throws, y):
    return throws.count(y)*y

score_func = {
    States.long_straight: lambda x: 40,
    States.short_straight: lambda x: 30,
    States.full_house: lambda x: 25,
    States.yatzee: lambda x: 50,
    States.ones: lambda x: xes_score(x, 1),
    States.twos: lambda x: xes_score(x, 2),
    States.threes: lambda x: xes_score(x, 3),
    States.fours: lambda x: xes_score(x, 4),
    States.fives: lambda x: xes_score(x, 5),
    States.sixes: lambda x: xes_score(x, 6),
    States.four_total: lambda x: sum(x),
    States.three_total: lambda x: sum(x)
}


def gen_throws():
    return [random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6),
            random.randint(1, 6)
            ]



def check_throw(throw):
    throw = sorted(throw)
    results = list()

    if throw[0] == throw[1] == throw[2]  == throw[3] == throw[4]:
        results.append((States.yatzee,
                       score_func[States.yatzee](throw)
                       ))

    if 1 in throw:
        results.append((States.ones,
                       score_func[States.ones](throw)
                       ))
    if 2 in throw:
        results.append((States.twos,
                       score_func[States.twos](throw)
                       ))
    if 3 in throw:
        results.append((States.threes,
                       score_func[States.threes](throw)
                       ))
    if 4 in throw:
        results.append((States.fours,
                       score_func[States.fours](throw)
                       ))
    if 5 in throw:
        results.append((States.fives,
                       score_func[States.fives](throw)
                       ))
    if 6 in throw:
        results.append((States.sixes,
                       score_func[States.sixes](throw)
                       ))

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw or \
        2 in throw and 3 in throw and 4 in throw and 5 in throw or \
        3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append((States.short_straight,
                       score_func[States.short_straight](throw)
                       ))

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw and 5 in throw or \
        2 in throw and 3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append((States.long_straight,
                       score_func[States.long_straight](throw)
                       ))
    if throw[0] == throw[1] == throw[2] and throw[3] == throw[4] or \
        throw[0] == throw[1] and throw[2] == throw[3] == throw[4]:
        results.append((States.full_house,
                        score_func[States.full_house](throw)
                        ))
    return results