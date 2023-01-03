# Function to check if the solution of sudoku puzzle is valid (so far) or not
def isValidSudoku(board):
   
  N = 9 
  zero = 0
  # Stores unique value
  # from 1 to N
  unique = [False] * (N + 1)
  
  
  # Traverse each column of
  # the given array
  for i in range(0, N):
     
    # Initialize unique[]
    # array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each row
    # of current column
    for j in range(0, N):
       
      # Stores the value
      # of board[j][i]
      Z = board[j][i] 
 
      if Z == 0:
        zero += 1
        
      # Check if current column
      # stores duplicate value
      if (unique[Z] == True and Z != 0):
        return False
       
      unique[Z] = True
 
  # Traverse each row of
  # the given array
  for i in range(0, N):
     
    # Initialize unique[]
    # array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each column
    # of current row
    for j in range(0, N):
       
      # Stores the value
      # of board[i][j]
      Z = board[i][j] 
      if Z == 0:
        zero += 1
      # Check if current row
      # stores duplicate value
      if (unique[Z] == True and Z != 0):
        return False
       
      unique[Z] = True
 
 
  # Traverse each block of
  # size 3 * 3 in board[][] array
  for i in range(0, N - 2, 3):
     
    # j stores first column of
    # each 3 * 3 block
    for j in range(0, N - 2, 3):
       
      # Initialize unique[]
      # array to false
      for m in range(0, N + 1):
        unique[m] = False
 
      # Traverse current block
      for k in range(0, 3):
        for l in range(0, 3):
           
          # Stores row number
          # of current block
          X = i + k
 
          # Stores column number
          # of current block
          Y = j + l
 
          # Stores the value
          # of board[X][Y]
          Z = board[X][Y]
          
          if Z == 0:
            zero += 1
          # Check if current block
          # stores duplicate value
          if (unique[Z] == True and Z != 0):
            return False
           
          unique[Z] = True
           
  # If all conditions satisfied
  if(zero > 0):
      return "You're doing great keep up !!"
  else:
      return True
 	
# This code is contributed by akhilsaini
