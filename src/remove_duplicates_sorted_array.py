# Solved
from typing import List, Union


arr = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def remove_duplicates(self, nums: List[Union[str, int]]):
        unique_elems = set()
        k = 0

        for i, num in enumerate(nums):
            if not num in unique_elems:
                unique_elems.add(num)
                nums[k] = num
                k += 1
            else:
                nums[i] = '_'
        return k

sol = Solution()
res_k = sol.remove_duplicates(arr)
print(res_k)
print(arr)

