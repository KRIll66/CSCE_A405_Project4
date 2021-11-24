from heuristics import mvr, lcv
from utils import is_consistent, assign, unassign

def backtrack_recurr(assignment, sudoku):

 
    if len(assignment) == len(sudoku.cells):
        return assignment

    cell = mvr(assignment, sudoku)

    for value in lcv(sudoku, cell):  

        if is_consistent(sudoku, assignment, cell, value):         
            assign(sudoku, cell, value, assignment)
            result = backtrack_recurr(assignment, sudoku)

            if result:
                return result

            unassign(sudoku, cell, assignment)
   
    return False