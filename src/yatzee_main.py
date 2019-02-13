

from externs import check_throw
from externs import check_score
from externs import scoring

from player import Player

from probability import chances

from itertools import combinations_with_replacement

playerone = Player("playerone")


for throw in combinations_with_replacement(range(1,7), 5):

    print(throw)
    scoring.temp_repr(check_score(throw,
                                  check_throw(throw)
                                  ))
    print( chances(throw) )
