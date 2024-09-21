from typing import List

def pivotIndex(nums: List[int]) -> int:
    left_sum = sum(nums)
    if left_sum == 0:
        return 0
    else:
        i = 1
        while i < len(nums):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
            i+=1
    return -1




a = [2, -1, -1]
a = [1, 7, 1, 9]
res = pivotIndex(a)
print(res)