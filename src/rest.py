

import numpy
import math
from scipy import stats
import numbers


def thing(asdf):
    asdf2 = []
    for i in range(0, len(asdf), 10):
        asdf2.append(asdf[i])
#    print("1", len(asdf2), len(asdf))
    return asdf2

def compression(asdf):
    temp = asdf
    while True:
        if len(temp) <= 1000:
            break
        else:
            temp = thing(temp)
    return temp

def false_in_gearsets(gearsets):
    for s in gearsets:
        if s.count(False) > 0:
            return True
    return False

def generate_printable_stats(stat, cost):
    
    cost = math.ceil(cost/1000)
    
    mean = numpy.mean( stat )
    print(    " Mean : %d [%dk tokens]" % ( mean, numpy.ceil(mean*cost) ) )
    
    mode = stats.mode( stat )[0]
    print(    " Mode : %d [%dk tokens]" % ( mode, numpy.ceil(mode*cost) ) )
    
    min = numpy.min( stat )
    print(    " Min  : %d [%dk tokens]" % ( min, numpy.ceil(min*cost) ) )
    
    max = numpy.max( stat )
    print(    " Max  : %d [%dk tokens]" % ( max,numpy.ceil( max*cost) ) )
    
    
    
from struct import unpack
from os import urandom


    
def overcomplexrandom():
    
    number = abs(unpack("d",urandom(8))[0])
    
    number = abs( math.modf(math.log10(number))[0] )
    
    return number

def reuserandom(x):
    return x*1000 % 1

