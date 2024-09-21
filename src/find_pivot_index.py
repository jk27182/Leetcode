def pivot_index(nums):
    left_sum = 0
    right_sum = sum(nums) - nums[0]
    print('beginning', left_sum, right_sum)
    if nums[0] == right_sum:
        return 0
    for i in range(1, len(nums) - 1):
        left_sum = left_sum + nums[i-1]
        right_sum = right_sum - nums[i]
        print('iter ', i, left_sum, right_sum)
        if left_sum == right_sum:
            return i
            
    return -1

inp = [1,7,3,6,5,6]

print(pivot_index(inp))