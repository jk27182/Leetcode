from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 1:
        return matrix[0]
    
    if cols == 1:
        return [row[0] for row in matrix]
    
    start_row = 0
    start_col = 0

    left = 0
    right = cols-1
    top = 0
    down = rows-1

    res = []
    # rechts
    while top <= down or left <= right:
        for col in range(left, right+1):
            res.append(matrix[top][col])
        top+=1
        # unten
        for row in range(top, down+1):
            res.append(matrix[row][right])
        right-=1

        # links
        for col in reversed(range(left, right+1)):
            print(f"{col=}")
            res.append(matrix[down][col])
        down-=1
        
        # oben
        for row in reversed(range(top, down+1)):
            res.append(matrix[row][left])
        left+=1

    return res


matrix = [[1,2,3], [4,5,6], [7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1,2],[3,4]]
print(spiralOrder(matrix))