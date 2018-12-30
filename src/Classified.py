from random import random
import numpy
import math
import rest
from scipy import stats

from rest import false_in_gearsets
from rest import generate_printable_stats



def Global_event_Classified_Single_Set(gearsets, tries):
    event_sets = set()
    while len(event_sets) < 4:
        event_sets.add(int(random()*14))
        
    event_sets = numpy.sort(list( event_sets ), kind = 'mergesort')
    
    sets_done = [False]
    
    while True:
        tries += 1
        
        
        
        drop_set = event_sets[0]
        drop_item = int( random()*6 )
        
        
        
        
        if gearsets[drop_set][drop_item] == True:
            pass
        else:
            gearsets[drop_set][drop_item] = True
                    
                    
                            
        if False not in gearsets[event_sets[0]]:
            sets_done[0] = True
        
        if False not in sets_done:
            break   
    
    
    return gearsets, tries



def Global_event_Classified(gearsets, tries):
    event_sets = set()
    while len(event_sets) < 4:
        event_sets.add(int(random()*14))
        
#    event_sets = numpy.sort(list( event_sets ), kind = 'mergesort')
    event_sets = list( event_sets )
    
    sets_done = [False]*4
    
#    print( event_sets )
#    print( gearsets[event_sets[0]], gearsets[event_sets[1]], gearsets[event_sets[2]], gearsets[event_sets[3]] )
        
    
    while True:
        
        drop_set = event_sets[ int( random()*4 ) ]
        drop_item = int( random()*6 )
        
        if False not in gearsets[event_sets[0]]:
            sets_done[0] = True
            if False not in gearsets[event_sets[1]]:
                sets_done[1] = True
                if False not in gearsets[event_sets[2]]:
                    sets_done[2] = True
                    if False not in gearsets[event_sets[3]]:
                        sets_done[3] = True
        
        if False not in sets_done:
            break     
        
        if False not in gearsets[drop_set]:
            continue
        
#        print( drop_set, drop_item)
#        print( gearsets[event_sets[0]], gearsets[event_sets[1]], gearsets[event_sets[2]], gearsets[event_sets[3]] )
#        print( sets_done )
        
        
        tries += 1
        
        
        if gearsets[drop_set][drop_item] == True:
            pass
        else:
            gearsets[drop_set][drop_item] = True
    
    
    return gearsets, tries





def ClassifiedGE( max_tries, events = -1 ):

    print("ClassifiedGE", max_tries, events)

    results_tries = []
    

    for dummy in range(max_tries):
        
        if dummy%1000 == 0:
            print(dummy)

        gearsets = [None]*14
        for index in range(len(gearsets)):
            gearsets[index] = [False]*6
            
        tries = 0 
        
        
        if events == 0:
            gearsets, tries = Global_event_Classified_Single_Set(gearsets, tries)
            
        elif events == 1:
            gearsets, tries = Global_event_Classified(gearsets, tries)
            
        elif events == 2: 
            while false_in_gearsets(gearsets):
#                print("-")
#                print(gearsets)
                gearsets, tries = Global_event_Classified(gearsets, tries)


            

        results_tries.append( tries )

    print("Finished the for loop")
    
    generate_printable_stats(results_tries, 3000)
    
    return results_tries











