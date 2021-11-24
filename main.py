import urllib.request, ac3
from sudoku import Sudoku
from backtrack import backtrack_recurr
from utils import generate_sudoku_grids, print_grid

"""
A program that solves sudoku puzzles using constraint satisfaction. 
Constraint Propagation using the AC3 algorithm, and backtracking should AC3 not be able to solve the puzzle.

The program will ask the user to enter a path to a .txt file in order to populate the Sudoku puzzle. 
The user will have the option of entering a web domain or a path to a local text file. 
Once the values are read into the program, the program automatically begins to solve the puzzle.

Marshall Pratt - marshallpratt1@yahoo.com
Chris Hill     - rhil66@alaska.edu
Lydia Stark    - lydiastark@gmail.com


inspirations & references:

https://github.com/ishpreet-singh/Sudoku
https://github.com/speix/sudoku-solver/blob/master/sudoku.py
https://sandipanweb.files.wordpress.com/2017/03/im31.png
https://cs.stackexchange.com/questions/47870/what-is-least-constraining-value
http://aima.cs.berkeley.edu/python/csp.html

"""


def solver(grid):
    
    print("\nSudoku: \n{}".format(print_grid(grid)))
    print("AC3 starting...")

    sudoku = Sudoku(grid)
    AC3_result = ac3.AC3(sudoku)

    if not AC3_result:
        print("No solution exists!")

    else:

        if sudoku.isFinished():

            print("AC3 was able to solve the sudoku!")
            print("Result: \n{}".format(sudoku))

        else:

            print("AC3 terminated without solution. \nBacktracking starting...")

            assignment = {}

            for cell in sudoku.cells:

                if len(sudoku.domain[cell]) == 1:
                    assignment[cell] = sudoku.domain[cell][0]
            
            assignment = backtrack_recurr(assignment, sudoku)
            
            for cell in sudoku.domain:
                sudoku.domain[cell] = assignment[cell] if len(cell) > 1 else sudoku.domain[cell]
            
            if assignment:
                print("AC3 with Backtracking was able to solve the sudoku!")
                print("Result: \n{}".format(sudoku))

            else:
                print("No solution exists!")


if __name__ == "__main__":
    sudoku_string = ""
    #get user input for file location
    while True:
        input_type = input("To use a .txt from a web domain, press 1;\nTo use a .txt from a local directory, press 2;\n")    
        try:
            input_type = int(input_type)
            if input_type == 1:
                file_path = input("Paste the file domain:\n")
                break
            if input_type == 2:
                file_path = input("Paste the file path:\n")
                break
            if input_type > 2 or input_type < 1:
                print ("Your input is out of range...")
        except:
            print("The input must be an integer...")
        
    file_path.strip()    

    if input_type == 1:
        file = urllib.request.urlopen(file_path)
        for line in file:
            decoded_line = line.decode("utf-8")
            for value in decoded_line:
                if value != " " and value != "\n":    
                    sudoku_string += value
    else:
        file = open(file_path)
        for line in file:                
            for value in line:
                if value != " " and value != "\n":
                    sudoku_string += value

        
    sudoku_queue = generate_sudoku_grids(sudoku_string)

    for index, sudoku_grid in enumerate(sudoku_queue):
        solver(sudoku_grid)