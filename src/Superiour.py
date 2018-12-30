from random import random
import numpy
import math
from scipy import stats

from rest import false_in_gearsets
from rest import generate_printable_stats



def Global_event_Superiour(gearsets, tries):

    event_sets = set()
    while len(event_sets) < 4:
        event_sets.add(int(random()*14))
        
    event_sets = list( event_sets )
    
    
    
    
    while True:
        tries += 1
        
        
        drop_set = event_sets[ int( random()*4 ) ]
        drop_item = int( random()*6 )
        if random() <= (0.45):
            if gearsets[drop_set][drop_item] == True:
                pass
            else:
                gearsets[drop_set][drop_item] = True
        
        drop_set = event_sets[ int( random()*4 ) ]
        drop_item = int( random()*6 )
        if random() <= (0.45):
            if gearsets[drop_set][drop_item] == True:
                pass
            else:
                gearsets[drop_set][drop_item] = True
        
        drop_set = event_sets[ int( random()*4 ) ]
        drop_item = int( random()*6 )
        if random() <= (0.125):
            if random() <= (0.90):
                if gearsets[drop_set][drop_item] == True:
                    pass
                else:
                    gearsets[drop_set][drop_item] = True
                    
                    
        if False not in gearsets[event_sets[0]]:
            if False not in gearsets[event_sets[1]]:
                if False not in gearsets[event_sets[2]]:
                    if False not in gearsets[event_sets[3]]:
                        break          
    
    
    
    return gearsets, tries





def SuperiourGE( max_tries, events = -1 ):

    items = 6*4

    print("SuperiourGE", max_tries, events)

    results_tries = []
    
    #max_tries = 10**7*3 #(Estimated to be 9 hours......................)


    for dummy in range(max_tries):


        gearsets = [None]*14
        for index in range(len(gearsets)):
            gearsets[index] = [False]*6
            
        tries = 0 
        
        if events > 0:
            for i in range(events):
                gearsets, tries = Global_event_Superiour(gearsets, tries)
            
        else: 
            while false_in_gearsets(gearsets):
                gearsets, tries = Global_event_Superiour(gearsets, tries)


            

        results_tries.append( tries )

    print("Finished the for loop")
    
    generate_printable_stats(results_tries, 1500)
    
    return results_tries










