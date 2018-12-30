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
temp = ClassifiedGE(10**5, 2)


print("Done")

temp = numpy.sort(temp, kind = 'mergesort')

temp = compression(temp)






print("Plotting...")


fig = plt.figure()


#plt.scatter(range(len(temp)), temp)
#plt.plot(temp)
plt.bar(range(len(temp)), temp)

plt.show()

