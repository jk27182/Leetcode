from typing import List
from collections import defaultdict


def largestAltitude(gain: List[int]) -> int:
    # abs_map = {}
    # double_numbers = set()
    # max_altitude = 0
    # for marginal in gain:
    #     abs_marginal = abs(marginal)

    #     if abs_map.get(abs_marginal, False):
    #         double_numbers.add(abs_marginal)

    #     abs_map[abs_marginal] = True

     
    # for marginal in gain:
    #     if abs(marginal) in double_numbers:
    #         continue

    #     gain_up = max(marginal, 0)
    #     max_altitude += gain_up
    prefix = 1
    current_max_altitude = 0

    while prefix < len(gain) + 1:

        marignal_gain = sum(gain[:prefix])
        print(marignal_gain)
        if marignal_gain > current_max_altitude:
            current_max_altitude = marignal_gain
        prefix += 1 

    return current_max_altitude




gains = [-4,-3,-2,-1,4,3,2]
# gains = [-5,1,5,0,-7]
# gains = [52,-91,72]
gains = [28,0,-8,-99,11,62,-35,68,2,12,-71,13,66,-28] #49
res = largestAltitude(gains)
print('res', res)