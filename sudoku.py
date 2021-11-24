import itertools
import sys


rows = "123456789"
cols = "ABCDEFGHI"

class Sudoku:

    def __init__(self, grid):
        game = list(grid)
        
        
        self.cells = list()
        self.cells = self.generate_coords()

        
        self.possibilities = dict()
        self.possibilities = self.generate_possibilities(grid)
   
        
        rule_constraints = self.generate_rules_constraints()

        
        self.binary_constraints = list()
        self.binary_constraints = self.generate_binary_constraints(rule_constraints)

        
        self.related_cells = dict()
        self.related_cells = self.generate_related_cells()

        
        self.pruned = dict()
        self.pruned = {v: list() if grid[i] == '0' else [int(grid[i])] for i, v in enumerate(self.cells)}


    """
    generates all the coordinates of the cells
    """
    def generate_coords(self):

        all_cells_coords = []

        
        for col in cols:

            
            for row in rows:
                
                
                new_coords = col + row
                all_cells_coords.append(new_coords)

        return all_cells_coords

    """
    generates all possible value remaining for each cell
    """
    def generate_possibilities(self, grid):

        grid_as_list = list(grid)

        possibilities = dict()

        for index, coords in enumerate(self.cells):
            
            if grid_as_list[index] == "0":
                possibilities[coords] = list(range(1,10))
            
            else:
                possibilities[coords] = [int(grid_as_list[index])]

        return possibilities

    """
    generates the constraints based on the rules of the game:
    value different from any in row, column or square
    """
    def generate_rules_constraints(self):
        
        row_constraints = []
        column_constraints = []
        square_constraints = []

        
        for row in rows:
            row_constraints.append([col + row for col in cols])

        
        for col in cols:
            column_constraints.append([col + row for row in rows])


        rows_square_coords = (cols[i:i+3] for i in range(0, len(rows), 3))
        rows_square_coords = list(rows_square_coords)

        cols_square_coords = (rows[i:i+3] for i in range(0, len(cols), 3))
        cols_square_coords = list(cols_square_coords)

        
        for row in rows_square_coords:
            for col in cols_square_coords:

                current_square_constraints = []
                
                
                for x in row:
                    for y in col:
                        current_square_constraints.append(x + y)

                square_constraints.append(current_square_constraints)

        
        return row_constraints + column_constraints + square_constraints

    """
    generates the binary constraints based on the rule constraints
    """
    def generate_binary_constraints(self, rule_constraints):
        generated_binary_constraints = list()

        
        for constraint_set in rule_constraints:

            binary_constraints = list()   
            
            for tuple_of_constraint in itertools.permutations(constraint_set, 2):
                binary_constraints.append(tuple_of_constraint)

           
            for constraint in binary_constraints:


                constraint_as_list = list(constraint)
                if(constraint_as_list not in generated_binary_constraints):
                    generated_binary_constraints.append([constraint[0], constraint[1]])

        return generated_binary_constraints

    """
    generates the the constraint-related cell for each one of them
    """
    def generate_related_cells(self):
        related_cells = dict()
        
        for cell in self.cells:

            related_cells[cell] = list()
            
            for constraint in self.binary_constraints:
                if cell == constraint[0]:
                    related_cells[cell].append(constraint[1])

        return related_cells

    """
    checks if the Sudoku's solution is finished
    we loop through the possibilities for each cell
    if all of them has only one, then the Sudoku is solved
    """
    def isFinished(self):
        for coords, possibilities in self.possibilities.items():
            if len(possibilities) > 1:
                return False
        
        return True
    
    """
    returns a human-readable string
    """
    def __str__(self):

        output = ""
        count = 1
        
        
        for cell in self.cells:
            
            value = str(self.possibilities[cell])
            if type(self.possibilities[cell]) == list:
                value = str(self.possibilities[cell][0])

            output += "[" + value + "]"

            if count >= 9:
                count = 0
                output += "\n"
            
            count += 1
        
        return output
       
