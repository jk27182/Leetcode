from typing import List

# gas = [1,2,3,4,5], cost = [3,4,5,1,2]
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    # early exit: cost[i] > gas[i], dann hat man nicht genug gas für die nächste route
    # es muss immer cost[i] <= gas[i] gelten
    # requires to iterate in cyrcle if iter == len(gas): iter = 0

    # build sum, if sum > 0 return index, otherwise -1

    len_gas = len(gas)
    tank = 0
    idx = 0
    for i in range(len_gas):
        new_gas = gas[i] - cost[i]  
        tank += new_gas
        if tank < 0:
            tank = 0
            idx = i+1

    return idx if new_gas >= 0 else -1

# en route        
# new gas
#  -2, -4 . -6 . -3 0 
# -2,  -2 . -2 . 3 .3
# 0    1    2    3  4 
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# gas = [5,1,2,3,4] 
# cost = [4,4,1,5,1]
print(canCompleteCircuit(gas, cost))

#  1 . -2 . -1 . -3 . 0
#  1 . -3 . 1 .  -2  3
#  0   1 .  2 .  3 . 4 