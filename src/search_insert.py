from typing import List 
def search_insert(nums: List[int], target: int) -> int:
    def condition(idx) -> bool:
        return target < nums[idx]

    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left)//2
        
        if condition(mid):
            right = mid
        else:
            # links von mid wird die condition nicht erfüllt, die Condition kann also nur RECHTS von mid erfüllt werden
            left = mid +1

    return left

nums = [1,3,5,6]
target = 7
print(search_insert(nums, target))