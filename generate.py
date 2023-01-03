#Sudoku generator code
import random as rd
import backTrack as sk
import time

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]


# takes (9^(n*n))
def generate():
        #initialize l to (0,0)
    l = [0,0]
    
        # if no empty location, grid is generated, return true
    if not sk.find_empty_location(grid, l):
        return True
        # assign the empty position to row,col
    row = l[0]
    col = l[1]
        
        #generete a 9 unique random elements set of range 1,9
    sample = rd.sample(range(1,10),9) #O(9), number of possible solutions
    for num in sample: #iterate over the sample O(n)
            # if number is valid, place it in the grid
        if(sk.check_location_is_safe(grid, row, col, num)): #O(1)
            grid[row][col] = num
                
            if (generate()): # O(n*n), n*n = number of empty cells
                return True
                
        grid[row][col] = 0 #backtrack if no number is valid
    return False # allows backtracking

def game():
    t1 = time.time()
    generate()
    t2 = time.time()
    t3 = t2 - t1
    print("Runtime is " + str(t3) + " seconds")
    count = 55
    while count !=0:
        i = rd.randint(0,8)
        j = rd.randint(0,8)
        if(grid[i][j] != 0):
            count -= 1
            grid[i][j] = 0
    return grid
