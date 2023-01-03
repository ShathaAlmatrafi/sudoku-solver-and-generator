"""
 SUDOKU SOLVER PROJECT 'DRIVER CODE'
"""

# for the GUI
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font

# for the game
import generate # generate Sudoku puzzle
import solutionCheck as check # check the

# solving Algorithms
import backTrack as bt
import bruteForce as bf
import Search as s
import backtrack2 as b2



def solve():
    # window size and apperance
    window = tk.Toplevel(root)
    window.title("Sudoku Solver")
    window.geometry("400x400")
    icon = tk.PhotoImage(file= "sudoku.png")
    window.iconphoto(False, icon)
    window.config(bg = "honeydew2")
    
    
    solvedLabel = tk.Label(window, text = "",fg = "green", bg = 'honeydew2')
    solvedLabel.grid(row =15, column = 1, columnspan = 10, pady = 5)
    errlable = tk.Label(window, text = "",fg = "red", bg = 'honeydew2')
    errlable.grid(row =15, column = 1, columnspan = 10, pady = 5)

    grid = {}
    
    #solving algorithms
    def bruteForce():
        algo = 1
        getValues(algo)
    def backtrack():
        algo = 2
        getValues(algo)
    def backtrack2():
        algo = 3
        getValues(algo)
    def search():
        algo = 4
        getValues(algo)

    

    def validate(input):
        if(input.isdigit and len(input) <= 1 and input != "0"):
            return True
        elif(input == ""):
            return True
        else:
            return False
    reg = window.register(validate)

    def grid3x3(row,col,color):
        for i in range(3):
            for j in range(3):
                e = tk.Entry(window, width = 5, bg = color, justify = "center")
                e.config(validate = "key", validatecommand = (reg,"%P"))
                e.grid(row = row +1+i, column = col+j+1,padx = 1,pady = 1,ipady = 5)
                grid[(row+1+i,col+1+j)] = e
    
    def grid9x9():
        color = "#D0ffff"
        for rowNo in range(1,10,3):
            for colNo in range(0,9,3):
                grid3x3(rowNo,colNo,color)
                if color == "#D0ffff":
                    color = "#ffffd0"
                else:
                    color = "#D0ffff"
                    
    def clear():
        errlable.configure(text = "")
        solvedLabel.configure(text = "")
        for row in range(2,11):
            for col in range(1,10):
                cell = grid[(row,col)]
                cell.delete(0,"end")
                
                          
    def getValues(algo):
        board = [] 
        errlable.configure(text = "")
        solvedLabel.configure(text = "")
        for row in range(2,11):
            rows = []
            for col in range(1,10):
                val = grid[(row,col)].get()
                if val == "":
                    rows.append(0)
                else:
                    rows.append(int(val))
            board.append(rows)
        updateValues(board,algo)
        
    def updateValues(sudokuPuzzle,algo):
        if algo == 1:
            solve = bf.solver(sudokuPuzzle)
        elif algo == 2:
            solve = bt.solver(sudokuPuzzle)
        elif algo == 3:
           solve = b2.solver(sudokuPuzzle)
           pass
        else:
            solve = s.solver(sudokuPuzzle)
            pass
        if solve != "no":
            for rows in range(2,11):
              for col in range(1,10):
                  grid[(rows,col)].delete(0,"end")
                  grid[(rows,col)].insert(0,solve[rows-2][col-1])
            solvedLabel.configure(text="sudoku solved!")
        else:
            errlable.configure(text = "no solution available")
            
    grid9x9()
                

    label = tk.Label(window, text = "Enter your values to be solved.", bg = "honeydew2")
    label.grid(row = 0, column = 0, columnspan = 10)


    solve1 = tk.Button(window,command = bruteForce, text = "brute force", width = 13)
    solve1.place(relx=0.02, rely=0.85)
    #grid(row = 16,column = 1, columnspan = 2, pady = 3)

    solve2 = tk.Button(window,command = backtrack, text = "backtracking", width = 10)
    solve2.place(relx=0.28, rely=0.85)
    #grid(row = 16,column = 2, columnspan = 4, pady = 3)
    
    solve3 = tk.Button(window,command = backtrack2, text = "backtracking2", width = 10)
    solve3.place(relx=0.5, rely=0.85)
    #grid(row = 16,column = 4, columnspan = 5, pady = 3)
    
    solve4 = tk.Button(window,command = search, text = "Search", width = 13)
    solve4.place(relx=0.71, rely=0.85)
    #grid(row = 16,column = 8, columnspan = 8, pady = 3)

    clearb = tk.Button(window,command = clear, text = "Clear", width = 25)
    clearb.place(relx=0.02, rely=.93)
    #clearb.grid(row = 17,column = 0, columnspan = 10)

    exitb = tk.Button(window,command = window.destroy, text = "exit", width = 25)
    exitb.place(relx=0.5, rely=0.93)
    #exitb.grid(row = 17,column = 5, columnspan = 20, pady = 1) 
def play():
    window = tk.Toplevel(root)
    window.title("Sudoku Game")
    window.geometry("350x400")
    icon = tk.PhotoImage(file= "sudoku.png")
    window.iconphoto(False, icon)
    window.config(bg = "honeydew2")


    solvedLabel = tk.Label(window, text = "",fg = "green", bg = 'honeydew2')
    solvedLabel.grid(row =15, column = 1, columnspan = 10, pady = 5)
    errlable = tk.Label(window, text = "",fg = "red", bg = 'honeydew2')
    errlable.grid(row =15, column = 1, columnspan = 10, pady = 5)
    l = tk.Label(window, bg = 'honeydew2')
    grid = {}
    
    
    board = generate.game()

    def validate(input):
        if(input.isdigit and len(input) <= 1 and input != "0"):
            return True
        elif(input == ""):
            return True
        else:
            return False
    reg = window.register(validate)

    def grid3x3(row,col,color):
        for i in range(3):
            for j in range(3):
                if(board[i+row-1][col+j] == 0):
                    e = tk.Entry(window, width = 5, bg = color, fg= 'blue', justify = "center")
                    e.config(validate = "key", validatecommand = (reg,"%P"))
                    e.grid(row = row +1+i, column = col+j+1,padx = 1,pady = 1,ipady = 5)
                    grid[(row+1+i,col+1+j)] = e
                else:
                    x = str(board[i+row-1][j+col])
                    v = tk.StringVar(window, value = x)
                    e = tk.Entry(window, width = 5, disabledbackground = color, fg = "blue", justify = "center", textvariable = v)
                    e.config(validate = "key", validatecommand = (reg,"%P"), state = 'disabled')
                    e.grid(row = row+1+i, column = col+j+1,padx = 1,pady = 1,ipady = 5)
                    grid[(row+1+i,col+1+j)] = e
                       
    def grid9x9():
        color = "#D0ffff"
        for rowNo in range(1,10,3):
            for colNo in range(0,9,3):
                grid3x3(rowNo,colNo,color)
                if color == "#D0ffff":
                    color = "#ffffd0"
                else:
                    color = "#D0ffff"
                    
    def clear():
        errlable.configure(text = "")
        solvedLabel.configure(text = "")
        for row in range(2,11):
            for col in range(1,10):
                cell = grid[(row,col)]
                cell.delete(0,"end")
    
                    
    def getValues():
        board = [] 
        errlable.configure(text = "")
        solvedLabel.configure(text = "")
        l.config(text = "")
        for row in range(2,11):
            rows = []
            for col in range(1,10):
                val = grid[(row,col)].get()
                if val == "":
                    rows.append(0)
                else:
                    rows.append(int(val))
            board.append(rows)
        Checker(board)
        
    def Checker(sudokuPuzzle):
        valid = check.isValidSudoku(sudokuPuzzle)
        if valid == "You're doing great keep up !!":
            x = "You're doing great keep up !!"
        elif not valid:
            x = "you might want to check some of your inputs"
        else:
            x = "Well done!!!" 
        l.config(text = x)
        l.grid(row =15, column = 1, columnspan = 10, pady = 5)


    grid9x9()
    checkb = tk.Button(window,command = getValues, text = "check", width = 5)
    checkb.grid(row = 16,column = 4, columnspan = 5, pady = 1)

    clearb = tk.Button(window,command = clear, text = "Clear", width = 5)
    clearb.grid(row = 16,column = 1, columnspan = 2, pady = 1)
    
    resetb = tk.Button(window,command = play, text = "reset", width = 5)
    resetb.grid(row = 16,column = 2, columnspan = 3, pady = 1)
    
    exitb = tk.Button(window,command = window.destroy, text = "exit", width = 5)
    exitb.grid(row = 16,column = 3, columnspan = 4, pady = 1) 


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection



# Window 
root = tk.Tk()
root.title("Sudoku Project")
root.geometry("500x500")

# window icon
icon = tk.PhotoImage(file= "sudoku.png")
root.iconphoto(False, icon) 
root.config(bg = "magenta")


# window background image
image = Image.open('back.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill= 'both', expand = 'yes')



# navigating buttons
myFont = font.Font(family='Helvetica')

sol = tk.Button(root,command = solve, text = "solve", width = 15, fg = 'white', bg = 'steel blue')
sol.place(relx=0.5, rely=0.4, anchor= "center")
    
play1 = tk.Button(root,command = play, text = "play", width = 15, fg = 'white', bg = 'SlateBlue2')
play1.place(relx=0.5, rely=0.5, anchor= "center")
    
exitb = tk.Button(root,command = root.destroy, text = "exit", width = 15, fg = 'white', bg = 'violet red')
exitb.place(relx=0.5, rely=0.6, anchor= "center")
sol['font'] = myFont
play1['font'] = myFont
exitb['font'] = myFont   


root.mainloop()
