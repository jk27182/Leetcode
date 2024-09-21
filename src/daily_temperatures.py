from typing import List
# works but to slow
# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#     res = []
#     for left, baseline in enumerate(temperatures):
#         no_hotter_day = True
#         counter = 1
#         for compare_temp in temperatures[left+1:]:
#             print('left', left, 'baseline', baseline, 'comp_temp', compare_temp, 'counter', counter)
#             if baseline < compare_temp:
#                 res.append(counter)
#                 counter = 1
#                 no_hotter_day = False
#                 break
#             else:
#                 counter += 1 

#         if no_hotter_day:
#             res.append(0)
#     return res

# sliding window ansatz
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    left = 0
    right = 1
    len_temps = len(temperatures)
    counter = 1
    res = []
    while left < len_temps:
        if right == len_temps:
            res.append(0)
            left += 1
            right = left + 1
            counter = 1
            continue
        if temperatures[left] < temperatures[right]:
            res.append(counter)
            counter = 1
            left += 1
            right = left + 1
        else:
            right+=1
            counter+= 1

    return res


temps = [71,71,76,71,71,76,71,71,71,71,76,76,71,71,71]
# [1,1,4,2,1,1,0,0]

dailyTemperatures(temps)
