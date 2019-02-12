import math
import random

from enum import Enum
from enum import auto as enum_auto


class State(Enum):
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

class scoring:
    states_names = {
        State.yatzee: "Yatzee",
        State.full_house: "Full house",
        State.short_straight: "short straight",
        State.long_straight: "long straight",
        State.three_total: "Threes total",
        State.four_total: "Four_total",
        State.chance: "Chance",
        State.ones: "Ones",
        State.twos: "Twos",
        State.threes: "Threes",
        State.fours: "Fours",
        State.fives: "Fives",
        State.sixes: "Sixes"
    }

    @classmethod
    def temp_repr(cls, throw_states):
        for state, score in throw_states:
            print("\t %s %s"%(state,score))
        statemax, scoremax = cls.temp_max(throw_states)
        print("\t max: %s %d"%(statemax, scoremax))
        return

    @classmethod
    def temp_max(cls, throwstates):
        statemax, scoremax = 0,0
        for state, score in throwstates:
            if score > scoremax:
                statemax, scoremax = state, score
        return statemax, scoremax


    @staticmethod
    def xes_score(throws, y):
        return throws.count(y)*y


score_func = {
    State.long_straight: lambda x: 40,
    State.short_straight: lambda x: 30,
    State.full_house: lambda x: 25,
    State.yatzee: lambda x: 50,
    State.ones: lambda x: scoring.xes_score(x, 1),
    State.twos: lambda x: scoring.xes_score(x, 2),
    State.threes: lambda x: scoring.xes_score(x, 3),
    State.fours: lambda x: scoring.xes_score(x, 4),
    State.fives: lambda x: scoring.xes_score(x, 5),
    State.sixes: lambda x: scoring.xes_score(x, 6),
    State.four_total: lambda x: sum(x),
    State.three_total: lambda x: sum(x)
}






def check_throw(throw):
    throw = sorted(throw)
    results = list()

    if throw[0] == throw[1] == throw[2]  == throw[3] == throw[4]:
        results.append((State.yatzee,
                        score_func[State.yatzee](throw)
                        ))

    if 1 in throw:
        results.append((State.ones,
                        score_func[State.ones](throw)
                        ))
    if 2 in throw:
        results.append((State.twos,
                        score_func[State.twos](throw)
                        ))
    if 3 in throw:
        results.append((State.threes,
                        score_func[State.threes](throw)
                        ))
    if 4 in throw:
        results.append((State.fours,
                        score_func[State.fours](throw)
                        ))
    if 5 in throw:
        results.append((State.fives,
                        score_func[State.fives](throw)
                        ))
    if 6 in throw:
        results.append((State.sixes,
                        score_func[State.sixes](throw)
                        ))

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw or \
        2 in throw and 3 in throw and 4 in throw and 5 in throw or \
        3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append((State.short_straight,
                        score_func[State.short_straight](throw)
                        ))

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw and 5 in throw or \
        2 in throw and 3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append((State.long_straight,
                        score_func[State.long_straight](throw)
                        ))
    if throw[0] == throw[1] == throw[2] and throw[3] == throw[4] or \
        throw[0] == throw[1] and throw[2] == throw[3] == throw[4]:
        results.append((State.full_house,
                        score_func[State.full_house](throw)
                        ))
    return results