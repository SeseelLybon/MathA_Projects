from itertools import permutations

from viable_combi import ViableCombi
from collections import Counter

wishlist = {
            "Nimbatus": 13.43,
            "The First Tree": 6.69,
            "Heat Signature": 6.49,
            "STALKER": 4.79,
            "Watch_Dogs 2": 11.99,
            "Murdered": 2.99,
            "Exapunks": 13.43
            }

wishlist_rev = dict()

print("Sum:", sum(wishlist.values()))

for key, value in wishlist.items():
    wishlist_rev[value] = key

viable_combinations = set()

for perm in permutations(wishlist.values()):
    for i in range(len(perm)):
        if sum(perm[0:i]) >= 30:
            viable_combinations.add(
                ViableCombi(perm[0:i], perm[i:]))
            break

leftover_combinations = list()

for perm in viable_combinations:
    perm = sorted(perm)
    for perm2 in leftover_combinations:
        pass


'''
for i in viable_combinations:
    if sum(i.back) >= 29:
        print(i.front)
        print(round(sum(i.front), 2))
        print("\t", i.back)
        print("\t", round(sum(i.back), 2))
'''
