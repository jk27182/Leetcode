def array_except_self(nums):
    left_prods = [1]
    right_prods = [1]

    left_prod = 1
    for num in nums[:-1]:
        left_prod *= num
        left_prods.append(left_prod)
    print(left_prods)

    right_prod = 1
    for num in reversed(nums[1:]):
        right_prod *= num
        right_prods.append(right_prod)
    print(right_prods)


    res = []
    for left, right in zip(left_prods, reversed(right_prods)):
        res.append(left * right)

    return res


nums = [1,2,3,4]
# Output: [24,12,8,6]
print(array_except_self(nums))