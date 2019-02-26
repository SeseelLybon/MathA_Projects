import math
import random

from enum import Enum
from enum import auto as enum_auto

from collections import Counter

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
#        statemax, scoremax = cls.temp_max(throw_states)
#        print("\t max: %s %d"%(statemax, scoremax))
        return

    @classmethod
    def temp_max(cls, throwstates) -> tuple:
        statemax, scoremax = 0,0
        for state, score in throwstates:
            if score > scoremax:
                statemax, scoremax = state, score
        return statemax, scoremax


    @staticmethod
    def xes_score(throws, y) -> int:
        return throws.count(y)*y


score_func = {
    State.yatzee: lambda x: 50,
    State.long_straight: lambda x: 40,
    State.short_straight: lambda x: 30,
    State.full_house: lambda x: 25,
    State.ones: lambda x: scoring.xes_score(x, 1),
    State.twos: lambda x: scoring.xes_score(x, 2),
    State.threes: lambda x: scoring.xes_score(x, 3),
    State.fours: lambda x: scoring.xes_score(x, 4),
    State.fives: lambda x: scoring.xes_score(x, 5),
    State.sixes: lambda x: scoring.xes_score(x, 6),
    State.four_total: lambda x: sum(x),
    State.three_total: lambda x: sum(x)
}




def check_score(throw, states):
    return [ tuple([state, score_func[state](throw)] ) for state in states ]





def check_throw(throw):
    throw = sorted(throw)
    results = list()

    cntr = Counter(throw)

    if 2 in cntr.values() and 3 in cntr.values():
        results.append(State.full_house)
    if 3 in cntr.values():
        results.append(State.three_total)
    if 4 in cntr.values():
        results.append(State.four_total)
    if 5 in cntr.values():
        results.append(State.yatzee)

    if 1 in throw:
        results.append(State.ones)
    if 2 in throw:
        results.append(State.twos)
    if 3 in throw:
        results.append(State.threes)
    if 4 in throw:
        results.append(State.fours)
    if 5 in throw:
        results.append(State.fives)
    if 6 in throw:
        results.append(State.sixes)

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw or\
            2 in throw and 3 in throw and 4 in throw and 5 in throw or\
            3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append(State.short_straight)

    if 1 in throw and 2 in throw and 3 in throw and 4 in throw and 5 in throw or \
            2 in throw and 3 in throw and 4 in throw and 5 in throw and 6 in throw:
        results.append(State.long_straight)

    return results