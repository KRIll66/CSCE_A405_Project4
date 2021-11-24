import sys


"""
checks if the value is consistent in the assignments
"""
def is_consistent(sudoku, assignment, cell, value):

    is_consistent = True

    for current_cell, current_value in assignment.items():
            
        if current_value == value and current_cell in sudoku.related_cells[cell]:
            is_consistent = False
    

    return is_consistent


def unassign(sudoku, cell, assignment):
    
    if cell in assignment:
        for (coord, value) in sudoku.pruned[cell]:
            sudoku.domain[coord].append(value)
    
        sudoku.pruned[cell] = []
        del assignment[cell]


def assign(sudoku, cell, value, assignment):
    
    assignment[cell] = value

    if sudoku.domain:
        forward_checker(sudoku, cell, value, assignment)


def forward_checker(sudoku, cell, value, assignment):
    
    for related in sudoku.related_cells[cell]:
        if related not in assignment:
            if value in sudoku.domain[related]:       
                sudoku.domain[related].remove(value)
                sudoku.pruned[cell].append((related, value))


def generate_sudoku_grids(input):

        DEFAULT_SIZE = 81
        if (len(input) % DEFAULT_SIZE) != 0:
                print("Error : the string must be a multiple of {}".format(DEFAULT_SIZE))
                sys.exit()
        
        else:
                if not input.isdigit():
                        print("The input must be an integer...")
                        sys.exit()
                
                else:
                        return [input[i:i+DEFAULT_SIZE] for i in range(0, len(input), DEFAULT_SIZE)]

def print_grid(grid):

        output = ""
        count = 1
        for cell in grid:
            value = cell
            output += " " + value + " "

            if count >= 9:
                count = 0
                output += "\n"
            
            count += 1
        
        return output