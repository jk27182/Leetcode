def prod_array_except_self(nums):
    def multiply(arr):
        res = 1
        for num in arr:
            res *= num
        return res

    prod_arr = []
    for i, num in enumerate(nums):
        left = nums[:i]
        right = nums[i+1:]
        print('left',left)
        print('right', right)
        product = multiply(left) * multiply(right)
        prod_arr.append(product)

    return prod_arr

inp = [1,2,3,4]
res = prod_array_except_self(inp)
print(res)