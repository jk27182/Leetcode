from collections import defaultdict

# def validate_sudoku(board):
#     col_dict = defaultdict(set)
#     square_counter = 1
#     for row_number, row in enumerate(board):
#         row_set = set()
#         for col_number, number in enumerate(row):
#             if number == '.':
#                 continue
#             if number in row_set or number in col_dict[col_number]:
#                 return False
#             row_set.add(number)
#             col_dict[col_number].add(number) 

#     # check boxes
#     for i in range(3):
#         rows = board[i:i+3]
#         for col, row in enumerate(rows):
#             box_values = set()
#             for j in range(3):
#                 curr_box_row_vals = set(row[j][i:i+3])
#                 if curr_box_row_vals in box_values:
#                     return False
#                 box_values |= (curr_box_row_vals)
#             # first_3_vals = set(row[0][i:i+3])
#             # second_3_vals = set(row[1][i:i+3])
#             # third_3_vals = set(row[2][i:i+3])
#     return True


def validate_sudoku(board):
    seen_entries = set()
    for row_num, row in enumerate(board):
        for col_num, number in enumerate(row):
            if number == '.':
                continue
            row_str = f'row_check {row_num}{number}'
            col_str = f'col_check {col_num}{number}'
            box_str = f'box_check {row_num // 3}{col_num // 3}{number}'
            if row_str in seen_entries or col_str in seen_entries or box_str in seen_entries:
                print(seen_entries)
                return False
            seen_entries.add(row_str)
            seen_entries.add(col_str)
            seen_entries.add(box_str)
    return True
                
board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
# # false
print(validate_sudoku(board))