from random import random
import numpy
import rest
from scipy import stats


def LZbosses( max_tries ):
    items = 6*14
    print("LZbosses", max_tries, items)

    results_tries = [None]*max_tries
    
    #max_tries = 10**7*3 #(Estimated to be 9 hours......................)

    for dummy in range(max_tries):
        if dummy%100 == 0:
            print("At try", dummy, rest.getruntime(),"Seconds")
        gearsets = [False]*items
        tries = 0

        while False in gearsets:
            tries += 1
            drop = int(random()*6)
            if drop <= (1/6):
                drop_classy = int(random()*items)
                if gearsets[drop_classy]:
                    pass
                else:
                    gearsets[drop_classy] = True

        results_tries[dummy] = tries

    print("Finished the for loop")
    
    mean = numpy.mean( results_tries )
    print(    " Mean : %d" % mean )
    
    mode = stats.mode( results_tries )[0]
    print(    " Mode : %d" % mode )
    
    mini = numpy.min( results_tries )
    print(    " Min : %d" % mini )
    
    maxi = numpy.max( results_tries )
    print(    " Max : %d" % maxi )
    
    return results_tries