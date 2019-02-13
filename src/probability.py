

from externs import check_throw
from externs import State

from collections import Counter

def chances(throw):
    throw = sorted(throw)
    states = check_throw(throw)

    cntr = Counter(throw)


    if State.yatzee not in states:
        print("\t\t Chance of a yatzee:")
        if len( cntr.values()) == 5:
            print("\t\t 4:", round( (1/6)**4 *100, 2))
        if 2 in cntr.values():
            print("\t\t 3:", round( (1/6)**3 *100, 2))
        if 3 in cntr.values():
            print("\t\t 2:", round( (1/6)**2 *100, 2))
        if 4 in cntr.values():
            print("\t\t 1:", round( (1/6) *100, 2))


    if State.full_house not in states:
        print("\t\t Chance of a full house:")
        # contains a b c d e
        # needs 2a b
        # roll c d e
        if len( cntr.values()) == 5:
            print("\t\t 3:", round( (1/6)*(1/6)*(2/6) *100, 2))

        # contains 2a 2b c
        # needs a or b
        # roll c
        if list(cntr.values()).count(2):
            print("\t\t 1:", round( (2/6) *100, 2))

        # contains a b4 | 3a b c
        # needs a       | b
        # roll b        | c
        if 4 in cntr.values() or \
                3 in cntr.values() and 2 not in cntr.values():
            print("\t\t 1:", round( (1/6) *100, 2))

        # contains 5a
        # need 2b
        # roll 2a
        if 5 in cntr.values():
            print("\t\t 2:", round( (1/6)*(1/6) *100, 2))


    if State.long_straight not in states:
        print("\t\t Chance of a long_straight:")
        if State.short_straight in states:

            # contains 2a b c d
            # needs e
            # roll a
            # 1 2 3 4 6 or 1 3 4 5 6
            if 1 in throw or 6 in throw:
                print("\t\t 2:", round( (1/6) *100, 2) )
            # 2 3 4 5 a
            else:
                print("\t\t 1:", round( (2/6) *100, 2) )

        # contains 2a 2b c | 3a b c
        # needs d e        | d e
        # roll a b         | 2a
        if list(cntr.values()).count(2) or \
                3 in cntr.values() and 2 not in cntr.values():
            print("\t\t 2:", round( (1/6)*(2/6) *100, 2))

        # contains a b4
        # needs c d e
        # roll 3b
        if 4 in cntr.values():
            print("\t\t 3:", round( (1/6)*(2/6)*(3/6) *100, 2))

        # contains 5a
        # need b c d e
        # roll 4a
        if 5 in cntr.values():
            print("\t\t 4:", round( (1/6)*(2/6)*(3/6)*(4/6) *100, 2))

    if State.short_straight not in states:
        print("\t\t Chance of a long_straight:")
        if State.short_straight in states:

        # contains 2a 2b c  | 3a b c
        # needs d           | d
        # roll a b          | 2a
        if list(cntr.values()).count(2) or \
                3 in cntr.values() and 2 not in cntr.values():
            print("\t\t 2:", round( (1-(5/6)*(5/6)) *100, 2))

        # contains a b4
        # needs c d
        # roll 3b
        if 4 in cntr.values():
            print("\t\t 3:", round( (1-(4/6)*(4/6)*(4/6)) *100, 2))

        # contains 5a
        # need b c d e
        # roll 4a
        if 5 in cntr.values():
            print("\t\t 4:", round( (1/6)*(2/6)*(3/6)*(4/6) *100, 2))