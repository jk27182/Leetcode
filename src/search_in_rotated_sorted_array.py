from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = left + (right - left) // 2

        # highest Element left of middle
        # print('left', left, 'middle', middle, 'right', right)
        if nums[left] > nums[middle]:
            if nums[left] <= target or nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        # highest Element right of middle or middle
        else:
            # left part will definetly be sorted, so check if its in the left
            if target <= nums[middle] and nums[left] <= target:
                right = middle
            else:
                left = middle + 1
        # print('after','left', left, 'middle', middle, 'right', right)
        
    return left if nums[left] == target else -1

# inp = [5,6,7,1]
# nums = [4,5,6,7,0,1,2]
nums = [1,2,3]
target = 7
print(search(nums, target))