

from externs import check_throw
from externs import State

from collections import Counter

def ftpt(x):
    return round( x*100, 2)


def chances(throw):
    throw = sorted(throw)
    states = check_throw(throw)

    cntr = Counter(throw)


    if State.yatzee not in states:
        print("\t\t Chance of a yatzee:")

        # p(a)*4
        if len( cntr.values()) == 5:
            print("\t\t 4:", ftpt( (1/6)**4 ))
        # p(a)*3
        if 2 in cntr.values():
            print("\t\t 3:", ftpt( (1/6)**3 ))
        # p(a)*2
        if 3 in cntr.values():
            print("\t\t 2:", ftpt( (1/6)**2 ))
        # p(a)
        if 4 in cntr.values():
            print("\t\t 1:", ftpt( (1/6) ))


    if State.full_house not in states:
        print("\t\t Chance of a full house:")
        # contains a b c d e
        # needs 2a && b
        # p(a) and p(a) and p(b) = (1-5/6)*(1-5/6)*(1-4/6)
        # roll c d e
        if len( cntr.values()) == 5:
            print("\t\t a b c d e -> c d e")
            print("\t\t 3:", ftpt( (1-5/6)*(1-5/6)*(1-4/6) ))

        # contains 2a 2b c
        # needs a || b
        # p(a) or p(b) = (1-4/6)
        # roll c
        if list(cntr.values()).count(2) == 2:
            print("\t\t 2a 2b c -> c")
            print("\t\t 1:", ftpt( (1-4/6) ))

        # contains 2a b c d
        # needs a & b
        # p(a and b) = (1/6)**2
        # roll c d
        if list(cntr.values()).count(2) == 1 and 3 not in cntr.values():
            prtft("2a b c d", "b c d")
            print("\t\t 2:", ftpt( (1/6)**2 ))

        # contains a b4 | 3a b c
        # needs a       | b
        # p( a ) = (1/6)
        # roll b        | c
        if 4 in cntr.values() or \
                3 in cntr.values() and 2 not in cntr.values():
            print("\t\t a b4 -> b || 3a b c -> c")
            print("\t\t 1:", ftpt( (1/6) ))

        # contains 5a
        # need 2b
        # P(b and b) = (1/6)*(1/6)
        # roll 2a
        if 5 in cntr.values():
            prtft("5a", "2a")
            print("\t\t 2:", ftpt( (1/6)*(1/6) ))



    if State.long_straight not in states:
        print("\t\t Chance of a long_straight:")
        if State.short_straight in states:

            # contains 1 2 3 4 6 | 1 3 4 5 6
            # needs 5            | 2
            # p(5) = (1/6)
            # roll 6             | 1
            if 1 in throw or 6 in throw:
                print("\t\t 1 2 3 4 6 -> 6|| 1 3 4 5 6 -> 1")
                print("\t\t 1:", ftpt( (1/6) ))
            # contains 2 3 4 5 a
            # needs 1 || 6
            # P(1 or 6) = (1-5/6)
            # roll a
            else:
                prtft("2 3 4 5 a", "a")
                print("\t\t 1:", ftpt( (1-5/6) ))


        # contains 2a 2b c
        # needs d && e
        # p(d and e) = (2/6)*(1/6)
        # roll a b
        if list(cntr.values()).count(2) == 2:
            print("\t\t 2a 2b c -> a b")
            print("\t\t 2:", ftpt( (2/6)*(1/6) ))

        # contains 3a b c
        # needs d && e
        # p(d and e) = (2/6)*(1/6)
        # roll 2a
        if 3 in cntr.values() and 2 not in cntr.values():
            print("\t\t", "3a b c", "->", "2a")
            print("\t\t 2:", ftpt( (2/6)*(1/6) ))



        # contains 3a b c with c-a <=4
        # needs d && e
        # p(d and e) = (1-4/6)
        # roll 2a
        if 3 in cntr.values() and 2 not in cntr.values() and throw[-1] - throw[1] <= 4:
            print("\t\t 3a b c with c-a <=4", "->", "2a")
            print("\t\t 2:", ftpt( (2/6)*(1/6) ))
        # contains 3a b c with c-a > 4
        # needs b && c && d
        # p(b and c and d) = (2/6)+(2/6)*(1/6)
        # roll 2a c
        elif 3 in cntr.values() and 2 not in cntr.values() and throw[-1] - throw[1] > 4:
            print("\t\t", "3a b c with c-a > 4", "->", "2a c")
            print("\t\t 3:", ftpt( (2/6)+(2/6)*(1/6) ))

        # contains 3a 2b with c-a <= 4
        # needs c %% d %% e
        # p(c and d and e) = (2/6)+(2/6)*(1/6)
        # roll 2a 1b
        if 3 in cntr.values() and 2 in cntr.values() and throw[-1] - throw[1] <= 4:
            print("\t\t", "3a 2b with c-a <= 4", "->", "2a 2b")
            print("\t\t 3:", ftpt( (3/6)*(2/6)*(1/6) ))
        # contains 3a 2b %% b-a > 4
        # needs b %% c %% d % e
        # p( b and c and d and e ) = (2/6)+(2/6)*(1/6)
        # roll 2a 2b
        if 3 in cntr.values() and 2 in cntr.values() and throw[-1] - throw[1] > 4:
            print("\t\t", "3a 2b %% b-a <= 4", "->", "2a 2b || 3a b")
            print("\t\t 4:", ftpt( (2/6)+(2/6)*(1/6) ))

        # contains a b4
        # needs c && d && e
        # p( c and d and e ) = (3/6)*(2/6)*(1/6)
        # roll 3b
        if 4 in cntr.values():
            print("\t\t a b4 -> 3b")
            print("\t\t 3:", ftpt( (3/6)*(2/6)*(1/6) ))

        # contains 5a
        # need b && c && d && e
        # p( b and c and d and e ) = (4/6)*(3/6)*(2/6)*(1/6)
        # roll 4a
        if 5 in cntr.values():
            print("\t\t 5a -> 4a")
            print("\t\t 4:", ftpt( (4/6)*(3/6)*(2/6)*(1/6) ))


    if State.short_straight not in states:
        print("\t\t Chance of a short_straight:")


        # contains 3a b c with c-a <=3
        # needs d
        # p( d ) = (1-5/6)**2
        # roll 2a
        if 3 in cntr.values() and 2 not in cntr.values() and throw[-1] - throw[1] <= 3:
            print("\t\t 3a b c with c-a <=3", "->", "2a")
            print("\t\t 2:", ftpt( (1-5/6)**2 ))
        # contains 3a b e with e-a > 3
        # needs c %% d
        # p(c and d) = (1-5/6)**2
        # roll 2a e
        elif 3 in cntr.values() and 2 not in cntr.values() and throw[-1] - throw[1] > 3:
            print("\t\t", "3a b c with c-a > 3", "->", "2a c")
            print("\t\t 3:", ftpt( (3/6)*(2/6)*(4/6) ))

        # contains 3a 2b with c-a <= 3
        # needs c && d
        # p( c and d ) = (3/6)*(2/6)*(5/6)
        # roll 2a 1b
        if 3 in cntr.values() and 2 in cntr.values() and throw[-1] - throw[1] <= 3:
            print("\t\t", "3a 2b with c-a <= 3", "->", "2a 1b")
            print("\t\t 3:", ftpt( (3/6)*(2/6)*(5/6) ))
        # contains 3a 2e %% e-a > 3
        # needs b %% c %% d
        # p( b and c and d ) = (3/6)*(3/6)*(2/6)
        # roll 2a 2e
        if 3 in cntr.values() and 2 in cntr.values() and throw[-1] - throw[1] > 3:
            print("\t\t", "3a 2b %% b-a <= 3", "->", "2a 2b || 3a b (Might be wrong)")
            print("\t\t 4:", ftpt( (3/6)*(3/6)*(2/6) ))


        # contains 2a 2b c
        # needs d
        # p(d) or p(d and e) = (1-4/6)+(2/6*1/6)
        # roll a b
        if list(cntr.values()).count(2) == 2 and throw[-1] - throw[1] <= 3:
            prtft("2a 2b", "a b")
            print("\t\t 2:", ftpt( (1-4/6)+(2/6*1/6) ))
        # contains 2a 2b c
        # needs c & d
        # p(c) and p(d) = 1/6+2/6*1/6
        # roll a b c
        elif list(cntr.values()).count(2) == 2 and throw[-1] - throw[1] > 3:
            prtft("2a 2b c", "a b c")
            print("\t\t 3:", ftpt( 1/6+2/6*1/6 ))

        # contains a b4
        # needs c & d
        # p( c and d ) = (3/6)*(2/6)*(5/6)
        # roll 3b
        if 4 in cntr.values():
            prtft("a b4","3b")
            print("\t\t 3:", ftpt( (3/6)*(2/6)*(5/6) ))

        # contains 5a
        # need b & c & d
        # p(b and c and d) = (3/6)*(3/6)*(2/6)
        # roll 4a
        if 5 in cntr.values():
            prtft("5a","4a")
            print("\t\t 4:", ftpt( (3/6)*(3/6)*(2/6) ))

def prtft( contains, roll ):
    print("\t\t", contains, "->", roll)