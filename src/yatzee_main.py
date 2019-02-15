

from externs import check_throw
from externs import check_score
from externs import scoring

from player import Player

from probability import chances

from itertools import combinations_with_replacement
from externs import State

playerone = Player("playerone")

'''
thing = {
        State.full_house: [],
        State.short_straight: [],
        State.long_straight: [],
        State.yatzee: [],
    }

for throw in combinations_with_replacement(range(1,7), 5):
    throw_states = check_throw(throw)
    for state in throw_states:
        if state in thing.keys():
            thing[state].append(throw)

for key, value in thing.items():
    print(key)
    for throw in value:
        print("\t", throw)
        chances(throw)
'''

'''
for throw in combinations_with_replacement(range(1,7), 5):

    print(throw)
    scoring.temp_repr(check_score(throw,
                                  check_throw(throw)
                                  ))
    print( chances(throw) )
'''

throw = None

if not throw:
    playerone.new_throw()
    throw = playerone.throw
else:
    playerone.throw = throw
    playerone.rethrow([0,1,1,0,1])
    throw = playerone.throw

print(sorted(throw))
scoring.temp_repr(check_score(throw,
                              check_throw(throw)
                              ))
print( chances(throw) )