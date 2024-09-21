def search_matrix(matrix, target):
    if matrix[0][0] > target or matrix[-1][-1] < target:
        return False
    left = (0,0) #(row, col)
    right = (len(matrix) - 1, len(matrix[0]) - 1) #(row, col)

    def search(left, right):
        left_val = matrix[left[0]][left[1]]
        right_val = matrix[right[0]][right[1]]

        is_left = False
        is_right = False

        if target <= matrix[left[0]][-1]:
            middle = (left[0], (left[1] + right[1]) // 2) 
            right = (left[0], len(matrix[0]) - 1)
        elif target >= matrix[right[0]][0]:
            middle = (right[0], (left[1] + right[1]) // 2) 
            left = (right[0], 0)
        else:
            middle = ((left[0] + right[0]) // 2, (left[1] + right[1]) // 2) 


        print('left', left, 'right', right, 'middle', middle)
        middle_val = matrix[middle[0]][middle[1]]

        if left_val == target or right_val == target or middle_val == target:
            return True
        if middle == left or middle == right:
            return False
        if middle_val < target and target <= right_val:
            is_right = search(middle, right)
        elif left_val <= target and target < middle_val: 
            is_left = search(left, middle)

        return is_left or is_right

    return search(left, right)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 5
print(search_matrix(matrix, target))