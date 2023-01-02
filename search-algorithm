import sys
from copy import deepcopy
import time 

'''Methode, we send him an Array named Matrix,
Creates new array named blank by taking the same size as the matrix
 and filling the new views with zeros in the matrix'''
 
def blankstates(matrix):
    blank = []
    length = len(matrix)
    for i in range(0, length):
        for j in range(0, length):
            if(matrix[i][j] == 0):
                temp = [i,j]
                blank.append(temp)
    return blank

''' It checks the rows and columns and uses the tow for
 loop and starts to compare the lookup, if there are duplicate
 numbers it deletes'''
 
def checkrowcol(b,matrix):
    row = b[0]
    inrow = []
    blankrow = matrix[row][:]
    val = [i+1 for i in range(0,9)]
    inrow = val
    for bl in blankrow:
        for v in inrow:
            if(v == bl):
                inrow.remove(v)
    col = b[1]
    for row in range(0,9):
        h = matrix[row][col]
        for i in inrow:
            if i ==h:
                inrow.remove(i)
    return inrow
''' Adding the row and the column and creat the box'''
def makebox(row,col):
    b = []
    for r in row:
        for c in col:
            t = [r,c]
            b.append(t)
    return b

'''Check the box and start filling in the new matrix blankrow'''

def getboxes(i,matrix):
    row = [[0,1,2],[3,4,5],[6,7,8]]
    col = [[0,1,2],[3,4,5],[6,7,8]]
    if i in row[0]:
        r = row[0]
        c = col[i]
    elif i in row[1]:
        r = row[1]
        c = col[i-3]
    elif i in row[2]:
        r = row[2]
        c = col[i-6]
    mb = makebox(r,c)
    return mb

box = dict()
def checkbox(b,matrix,inrowcol):
    blankrow = []
    for bo in box:
        if b in box[bo]:
            for col in box[bo]:
                r = col[0]
                c = col[1]
                blankrow.append(matrix[r][c])
            break
    for bl in blankrow:
        for i in inrowcol:
            if (str(i)==bl):
                inrowcol.remove(i)
    return inrowcol
        
def check(b,matrix):
    inrowcol = checkrowcol(b,matrix)
    inrowcol = checkbox(b,matrix,inrowcol)
    return inrowcol

'''And use the solver method to call all the methods and solve sudoku'''

def solve(matrix,blank,level):
 if (matrix != 'not a solution'):
   satisfy = 0
   if(len(blank)>0):
       for b in blank:
           valids = check(b,matrix)
           if (len(valids) == 1):
               satisfy = 1
               r = int(b[0])
               c = int(b[1])
               matrix[r][c] = int(valids[0])
           elif (len(valids)== 0):
               return 'not a solution'
       if satisfy==0:
           b = blankstates(matrix)
           values = check(b[0],matrix)
           for v in values:
               if v in check(b[0],matrix):
                r = b[0][0]
                c = b[0][1]
                matrix[r][c] = v
                mat = solve(deepcopy(matrix),blankstates(matrix),level+1)
            
                if (mat!='not a solution'):
                   matrix = mat
                   b = blankstates(matrix)  
                   if (len(b)==0):
                       return matrix
                   
       
   b = blankstates(matrix)
  # print('len:',b)
   if (len(b)==0):
       return matrix
   else:
       return solve(matrix,blankstates(matrix),level)
   
    
def solver(matrix):
    blank = blankstates(matrix)
    for i in range (0,9):
        box[i] = getboxes(i, matrix)
    t1 = time.time()
    matrix = solve(matrix,blank,1)
    t2 = time.time()
    t3 = t2 - t1
    print("Runtime is " + str(t3) + " seconds")
    return matrix
