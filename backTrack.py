# Sudoku solver using Backtracking agorithm
import time
N = 9
 
# this functions takes a 9x9 sudoku grid and searches for an empty position
# it modifies the entrys of l when found and returns zero. otherwise it returns False
def find_empty_location(grid, l): # O(n^2)
	for row in range(9): #O(n)
		for col in range(9): # o(n)
			if(grid[row][col]== 0): # o(1)
				l[0]= row # o(1)
				l[1]= col # o(1)
				return True
	return False

# check if num is already present in this row
def used_in_row(grid, row, num): # O(n)
	for i in range(9):
		if(grid[row][i] == num):
			return True # if found
	return False # otherwise

# checks if num is already present in this column
def used_in_col(grid, col, num): # O(n)
	for i in range(9):
		if(grid[i][col] == num):
			return True # if found
	return False #otherwise 

# checks if num in already present in the 3x3 subgrid
def used_in_box(grid, row, col, num): # o(n)
	for i in range(3): # o(sqrt(n))
		for j in range(3): # o(sqrt(n))
			if(grid[i + row][j + col] == num):
				return True # if found return True
	return False # if not return false


def check_location_is_safe(grid, row, col, num):
    # calls the functions to check that num is not present in the row,col or 3x3 subgrid
    w = not used_in_row(grid, row, num) 
    y = not used_in_col(grid, col, num)
    z = not used_in_box(grid, row - row % 3, col - col % 3, num)
    x = w and y and z 
    return x



#takes O(9^m)
def solve_sudoku(grid):
	# creat l that keeps track of the empty position
    l = [0, 0]

    #if no empty positions, then we've successfuly solved the puzzel and should return false
    if(not find_empty_location(grid, l)): #O(n^2)
        return True
	
	# assign the empty position to row and col
    row = l[0]
    col = l[1]
	
	# valid values 1 to 9
    for num in range(1, 10): #O(9) , 9 = possible inputs
		
		# if it could work
        if(check_location_is_safe(grid, #O(n)
						row, col, num)):
			
			# assign the first valid number
            grid[row][col]= num

			# recursive call until it returns True when the sudoku is solved
			# if it returnes False, this will lead to backtracking
            if(solve_sudoku(grid)): #O(m), m = number of empty cells
                return True

			# failure, unmake & try again
            grid[row][col] = 0
			
	# this triggers backtracking	
    return False

def solver(sudoku):
    t1 = time.time()
    if solve_sudoku(sudoku):
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        return sudoku
    else:
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        return "no"
