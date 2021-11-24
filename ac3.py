
""" Input:
   problem:
   (which consists of)
   A set of variables X
   A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, the possible values of x
   A set of binary constraints R2(x, y) on variables x and y that must be satisfied
   
 Output:
   True or False if problem has a solution
   Arc consistent domains for each variable."""

def AC3(problem):
    queue = list(problem.binary_constraints)

    while queue:
        (xi, xj) = queue.pop(0)

        if remove_inconsistencies(problem, xi, xj): 
            if len(problem.domain[xi]) == 0:
                return False
            
            for Xk in problem.related_cells[xi]:
                if Xk != xi:
                    queue.append((Xk, xi))
                    
    return True

def remove_inconsistencies(problem, cell_i, cell_j):

    removed = False
  
    for value in problem.domain[cell_i]:
        if not any([diff(value, poss) for poss in problem.domain[cell_j]]):
            problem.domain[cell_i].remove(value)
            removed = True

    return removed


"""
checks if two cells are not the same
"""
def diff(cell_i, cell_j):
    result = cell_i != cell_j
    return result