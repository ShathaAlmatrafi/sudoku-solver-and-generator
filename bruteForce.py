# Sudoku solver using Brute Force agorithm

# note: Time Complexity will be referred to as TC

import time
# Declaring the size of the 2D matrix 9*9
size = 9 #TC= O(1)
# Print the grids
def printing(array): #TC = O(n^2)
	for i in range(size): #TC = O(n)*( O(n)*O(1) )*O(1) = O(n^2)
		for j in range(size): #TC = O(n)
			print(array[i][j], end = " | ") #TC = O(1)
        #newline
		print() #TC = O(1)
#------------------------------------------------------------------
'''
isSafe is a boolean method that recieves a grid, a cell index, and a number to check 
if it's legal to assign the number in this position by testing Sudoku game rules
'''
def isSafe(grid, row, col, number): #TC = O(n^2)
    #The following 3 loops tests the cell's current row, column, and box

	# Check: if the same number is found in the similar row,
	# ---> return false
	for x in range(9):  #TC = O(n)*O(1)*O(1) = O(n)
		if grid[row][x] == number:  #TC = O(1)
			return False  #TC = O(1)

	# Check: if the same number is found in the similar column,
	# ---> return false
	for x in range(9):  #TC = O(n) * O(1) * O(1) = O(n)
		if grid[x][col] == number:
			return False

	# Check: if the same number is found in the similar box (3*3 matrix),
	# ---> return false
    #next two lines compute the box we are at based on cell's row & col indexes 
	startRow = row - row % 3 #TC = O(1)
	startCol = col - col % 3 #TC = O(1)
	for i in range(3): #TC = O(n) * ( O(n) * O(1) * O(1)) = O(n^2)
		for j in range(3):
			if grid[i + startRow][j + startCol] == number:
				return False
    # if no duplication occcured ---> return true
	return True #TC = O(1)
#------------------------------------------------------------------
'''
solveSudoku method recives a partially-fillled grid with the 1st cell index and fills all its
unassigned cells by testing all possible numbers (1-9) and assuring that requirements are met
'''
def solveSudoku(grid, row, col): #TC = O(n^2)

    # Check: if we have reached 8th row and 9th column
	# ---> return true; to avoid further backtracking
    if (row == size - 1 and col == size): #TC = O(1)
        return True #TC = O(1)
	
	# Check: if column value becomes 9,
	# ---> move to next row and reset column to 0
    if col == size: #TC = O(1)
        row += 1 #TC = O(1)
        col = 0 #TC = O(1)
	# Check: if the current grid's position of already contains value > 0,
    # ---> move (iterate) to next column
    if grid[row][col] > 0: #TC = O(1)
        return solveSudoku(grid, row, col + 1)
    for number in range(1, size + 1): #TC = O(n) * ( O(1) * O(1) ) = O(n)
		# Check: if placing the number (1-9) in the given row, col is safe 
        # --> we move to next column
        if isSafe(grid, row, col, number):	 #TC = O(1)
			# Assigning the number in the current grid's position (row,col)
			# and assuming the assigned number in the position is correct
            grid[row][col] = number #TC = O(1)

			# Checking for next possibility with next column
            if solveSudoku(grid, row, col + 1): #TC = O(1)
                return True #TC = O(1)

		# if our assumption was wrong ---> reset cell value to 0
		# so we can try next assumption with different number value
        grid[row][col] = 0 #TC = O(1)
    return False #TC = O(1)
#------------------------------------------------------------------

def solver(sudoku):
    t1 = time.time()
    if solveSudoku(sudoku,0,0):
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        return sudoku
    else:
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        return "no"
