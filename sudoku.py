import itertools

cols = "ABCDEFGHI"
rows = "123456789"

class Sudoku:

    def __init__(self, grid):
        
        self.cells = list()
        self.cells = self.get_coordinates()
        self.domain = dict()
        self.domain = self.generate_domain(grid)
        constraints = self.get_constraints()
        self.binary_constraints = list()
        self.binary_constraints = self.get_binary_constraints(constraints)
        self.related_cells = dict()
        self.related_cells = self.get_related_cells()
        self.pruned = dict()
        self.pruned = {v: list() if grid[i] == '0' else [int(grid[i])] for i, v in enumerate(self.cells)}


    """
    gets all the coordinates of the cells
    """
    def get_coordinates(self):

        all_cells = []

        for col in cols:

            for row in rows:
                new_coords = col + row
                all_cells.append(new_coords)

        return all_cells

    """
    gets all possible values remaining for each cell
    """
    def generate_domain(self, grid):

        glist = list(grid)
        domain = dict()

        for index, coordinates in enumerate(self.cells):
            if glist[index] == "0":
                domain[coordinates] = list(range(1,10))
            
            else:
                domain[coordinates] = [int(glist[index])]

        return domain

    """
    gets the constraints of the game where # must be different from any in row, column or square
    """
    def get_constraints(self):
        
        r_constraints = []
        c_constraints = []
        sq_constraints = []

        
        for row in rows:
            r_constraints.append([col + row for col in cols])
        
        for col in cols:
            c_constraints.append([col + row for row in rows])

        rows_sq_coords = (cols[i:i+3] for i in range(0, len(rows), 3))
        rows_sq_coords = list(rows_sq_coords)

        col_sq_coords = (rows[i:i+3] for i in range(0, len(cols), 3))
        col_sq_coords = list(col_sq_coords)

        for row in rows_sq_coords:
            for col in col_sq_coords:
                temp_sp_constraints = []
                
                for x in row:
                    for y in col:
                        temp_sp_constraints.append(x + y)

                sq_constraints.append(temp_sp_constraints)

        return r_constraints + c_constraints + sq_constraints

    """
    creates the binary constraints from teh ones above
    """
    def get_binary_constraints(self, constraints):
        b_constraints = list()
    
        for constraint in constraints:
            binary_constraints = list()   
            
            for constraint_tuple in itertools.permutations(constraint, 2):
                binary_constraints.append(constraint_tuple)
 
            for constraint in binary_constraints:
                constraint_as_list = list(constraint)
                if(constraint_as_list not in b_constraints):
                    b_constraints.append([constraint[0], constraint[1]])

        return b_constraints

    """
    gets the the constraint-related cell for each one of them
    """
    def get_related_cells(self):
        related= dict()
        
        for cell in self.cells:
            related[cell] = list()
            
            for constraint in self.binary_constraints:
                if cell == constraint[0]:
                    related[cell].append(constraint[1])

        return related

    """
    checks if the sudoku is finished

    """
    def isFinished(self):
        for domain in self.domain.items():
            if len(domain) > 1:
                return False
        return True
    
    """
    returns a grid as a string
    """
    def __str__(self):

        output = ""
        count = 1
   
        for cell in self.cells:
            value = str(self.domain[cell])
            if type(self.domain[cell]) == list:
                value = str(self.domain[cell][0])

            output += " " + value + " "

            if count >= 9:
                count = 0
                output += "\n"
            
            count += 1
        
        return output
       
