

from externs import check_throw
from externs import scoring

from player import Player

playerone = Player("playerone")

for i in range(50):
    print("---------", i)
    playerone.new_throw()
    print(playerone.throw)
    scoring.temp_repr(check_throw(playerone.throw))
    playerone.rethrow([1,0,1,0,1,0])
    print(playerone.throw)
    scoring.temp_repr(check_throw(playerone.throw))
    playerone.rethrow([0,1,0,1,0,1])
    print(playerone.throw)
    scoring.temp_repr(check_throw(playerone.throw))