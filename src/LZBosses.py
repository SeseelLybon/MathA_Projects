from random import random
import numpy
import math
import rest
from scipy import stats



def LZbosses( max_tries ):
    items = 6*14

    print("LZbosses", max_tries, items)

    results_tries = []
    results_duplicates = []
    
    #max_tries = 10**7*3 #(Estimated to be 9 hours......................)

    for dummy in range(max_tries):

        gearsets = [False]*items
        duplicates = 0
        tries = 0

        while False in gearsets:
            tries += 1
            drop = int(random()*6)
            if drop <= (1/6):
                drop_classy = int(random()*items)
                if gearsets[drop_classy] == True:
                    duplicates += 1
                else:
                    gearsets[drop_classy] = True

        results_tries.append( tries )
        results_duplicates.append( duplicates )

    print("Finished the for loop")
    
    mean = numpy.mean( results_tries )
    print(    " Mean : %d" % ( mean ) )
    
    mode = stats.mode( results_tries )[0]
    print(    " Mode : %d" % ( mode) )
    
    min = numpy.min( results_tries )
    print(    " Min : %d" % ( min) )
    
    max = numpy.max( results_tries )
    print(    " Max : %d" % ( max) )
    
    return results_tries