
"""
Most Constrained Variable (MRV) heuristic
"""
def mvr(assignment, sudoku):
    unassigned = []

    for cell in sudoku.cells:
        if cell not in assignment:
            unassigned.append(cell)

    criteria = lambda cell: len(sudoku.domain[cell])

    return min(unassigned, key=criteria)

"""
Least Constraining Value (LCV) heuristic
"""
def lcv(sudoku, cell):

    if len(sudoku.domain[cell]) == 1:
        return sudoku.domain[cell]

    criteria = lambda value: conflict_counter(sudoku, cell, value)
    return sorted(sudoku.domain[cell], key=criteria)


def conflict_counter(sudoku, cell, value):
    
    count = 0

    for related in sudoku.related_cells[cell]:
        if len(sudoku.domain[related]) > 1 and value in sudoku.domain[related]:
            count += 1

    return count