import urllib.request
from sudoku import Sudoku
from ac3 import AC3
from backtrack import recursive_backtrack_algorithm
from utils import fetch_sudokus, print_grid


def solve(grid, index, total):
    
    print("\nSudoku : \n{}".format(index, total, print_grid(grid)))


    print("AC3 starting".format(index, total))

    sudoku = Sudoku(grid)
    AC3_result = AC3(sudoku)


    if not AC3_result:
        print("This sudoku has no solution")

    else:

        if sudoku.isFinished():

            print("AC3 was enough to solve this sudoku !")
            print("Result: \n{}".format(index, total, sudoku))


        else:

            print("AC3 finished without solution. Backtracking starting...".format(index,total))

            assignment = {}

            for cell in sudoku.cells:

                if len(sudoku.possibilities[cell]) == 1:
                    assignment[cell] = sudoku.possibilities[cell][0]
            

            assignment = recursive_backtrack_algorithm(assignment, sudoku)
            

            for cell in sudoku.possibilities:
                sudoku.possibilities[cell] = assignment[cell] if len(cell) > 1 else sudoku.possibilities[cell]
            
            if assignment:
                print("Result: \n{}".format(index, total, sudoku))

            else:
                print("No solution exists".format(index, total))


if __name__ == "__main__":
    sudoku_grid_as_string = ""
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
                    sudoku_grid_as_string += value
    else:
        file = open(file_path)
        for line in file:                
            for value in line:
                if value != " " and value != "\n":
                    sudoku_grid_as_string += value

        
    sudoku_queue = fetch_sudokus(sudoku_grid_as_string)

    for index, sudoku_grid in enumerate(sudoku_queue):
        solve(sudoku_grid, index + 1, len(sudoku_queue))