from LZBosses import LZbosses

from Superiour import SuperiourGE

from Classified import ClassifiedGE

from rest import compression
from rest import false_in_gearsets

import math as math
import numpy as numpy

from scipy import stats

import matplotlib.pyplot as plt

print("start")






#LZbosses
#SuperiourGE
#ClassifiedGE

#SuperiourGE(10**6)
print("-----")
#temp = ClassifiedGE(10**5)


#temp = LZbosses(1000)
temp = ClassifiedGE(1000)


do_profile = False
if do_profile:
    import cProfile
    import re
    cProfile.run('SuperiourGE(10**3)')



print("Done")





do_graph = False
if do_profile:

    print("Plotting...")

    temp = numpy.sort(temp, kind = 'mergesort')

    temp = compression(temp)

    fig = plt.figure()
    #
    #plt.scatter(range(len(temp)), temp)
    #plt.plot(temp)

    plt.bar(range(len(temp)), temp)

    plt.show()
