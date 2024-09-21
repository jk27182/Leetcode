

def search(nums, target) -> int:
    length = len(nums)
    left = 0
    right = len(nums) -1
    while left <= right:
        idx = (left + right) // 2
        if nums[idx] == target:
            return idx
        elif nums[idx] < target:
            left = idx + 1
        else: # nums[idx] > target:
            right = idx - 1
    
    return -1


numbers = [-1,0,3,5,12]
target = 9
idx = search(numbers, target)
print(idx)
print(numbers[idx])
print(target == numbers[idx])