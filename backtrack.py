from heuristics import select_unassigned_variable, order_domain_values
from utils import is_consistent, assign, unassign

def recursive_backtrack_algorithm(assignment, sudoku):

 
    if len(assignment) == len(sudoku.cells):
        return assignment

    cell = select_unassigned_variable(assignment, sudoku)


    for value in order_domain_values(sudoku, cell):

        
        if is_consistent(sudoku, assignment, cell, value):

          
            assign(sudoku, cell, value, assignment)

           
            result = recursive_backtrack_algorithm(assignment, sudoku)

            
            if result:
                return result

           
            unassign(sudoku, cell, assignment)
   
    return False