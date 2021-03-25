import calcudoku

good_test = [[1, 2, 3, 4, 5], [2, 1, 4, 5, 3], [3, 4, 5, 1, 2],\
 [4, 5, 2, 3, 1] , [5, 3, 1, 2, 4]] 
bad_row_test = [[2, 2, 3, 4, 5], [1, 1, 4, 5, 3], [3, 4, 5, 1, 2],\
 [4, 5, 2, 3, 1] , [5, 3, 1, 2, 4]] 
bad_column_test = [[1, 2, 3, 4, 5], [1, 2, 4, 5, 3], [3, 4, 5, 1, 2],\
 [4, 5, 2, 3, 1] , [5, 3, 1, 2, 4]] 

# Validate Rows Test
assert calcudoku.validate_rows(good_test) 
assert not calcudoku.validate_rows(bad_row_test) 
assert calcudoku.validate_rows(bad_column_test) #nothing wrong with rows 

# Validate Cols Test
assert calcudoku.validate_cols(good_test) 
assert calcudoku.validate_cols(bad_row_test) #nothing wrong with cols 
assert not calcudoku.validate_cols(bad_column_test) 


cage_data = \
[[9, 3, 0, 5, 6],\
[7, 2, 1, 2],\
[10, 3, 3, 8, 13],\
[14, 4, 4, 9, 14, 19],\
[3, 1, 7],\
[8, 3, 10, 11, 16],\
[13, 4, 12, 17, 21, 22],\
[5, 2, 15, 20],\
[6, 3, 18, 23, 24]]

solution = [[3,5,2,1,4],[5,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]]
not_solution = [[3,5,2,1,4],[5,2,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]]
technical_solution = [[7,5,2,1,4],[1,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]]

# Validate Cages Test
assert calcudoku.validate_cages(solution,cage_data)
assert not calcudoku.validate_cages(not_solution,cage_data)
assert calcudoku.validate_cages(technical_solution,cage_data)

# Validate All Test
assert calcudoku.validate_all(solution,cage_data)
assert not calcudoku.validate_all(not_solution,cage_data)
assert not calcudoku.validate_all(technical_solution,cage_data)

