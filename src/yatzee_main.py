import math
import random

from externs import gen_throws
from externs import check_throw
from externs import temp_repr




for i in range(50):
    throws = gen_throws()
    print(throws)
    temp_repr(check_throw(throws))