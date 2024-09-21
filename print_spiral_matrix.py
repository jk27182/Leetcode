from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    col_upper_bound = len(matrix[0])
    col_lower_bound = 0
    row_upper_bound = len(matrix)
    row_lower_bound = 0
    # consider right and down as forward
    is_forward = True # otherwise left or up

    row = 0
    col = 0
    counter = 0
    while col_upper_bound>col_lower_bound and row_upper_bound>row_lower_bound:
        counter+=1
  
        # move left or right
        while col < col_upper_bound and col >= col_lower_bound:
            print(matrix[row][col])
            if is_forward:
                col+=1
            else:
                col-=1
        col = 0 if col < 0 else col_upper_bound -1  
        new_row_dir = 1 if is_forward else -1
        row = row + new_row_dir

        if counter % 2 == 0:
            col_upper_bound-=1
            col_lower_bound+=1
            row_upper_bound -=1
            row_lower_bound +=1
        # move up or down
        while row < row_upper_bound and row >= row_lower_bound:
            print(matrix[row][col])
            if is_forward:
                row+=1
            else:
                row-=1

        is_forward = not is_forward
        row = 0 if row < 0 else row_upper_bound -1  
        new_col_dir = 1 if is_forward else -1 
        col = col + new_col_dir


matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2],[3,4]]
spiralOrder(matrix)