from utils import is_different


def AC3(csp, queue=None):

    if queue == None:
        queue = list(csp.binary_constraints)

    while queue:

        (xi, xj) = queue.pop(0)

        if remove_inconsistent_values(csp, xi, xj): 

            if len(csp.possibilities[xi]) == 0:
                return False
            
            for Xk in csp.related_cells[xi]:
                if Xk != xi:
                    queue.append((Xk, xi))
                    
    return True

def remove_inconsistent_values(csp, cell_i, cell_j):

    removed = False
  
    for value in csp.possibilities[cell_i]:

        if not any([is_different(value, poss) for poss in csp.possibilities[cell_j]]):

            csp.possibilities[cell_i].remove(value)
            removed = True

    return removed
