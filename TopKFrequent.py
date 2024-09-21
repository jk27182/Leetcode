from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    for num in nums:
        if counter.get(num, False):
            counter[num] += 1
        else:
            counter[num] = 1

    res = sorted(counter.keys(), key= lambda x : counter[x], reverse=True)[:k]
    return res 

a = [1,1,1,1,2,2,2,2,3]
print(topKFrequent(a, 2))