import cell, urllib.request

class Sudoku_Board:
    def __init__(self):       

        #make a blank sudoku with cell objects
        self.s_board = []
        for i in range(81):
            #the stored index will be 0 based
            self.s_board.append(cell.Cell(0, i))  
        
        #the below are used to reference like rows by list 
        #and like columns by index
        self.A = []
        self.B = []
        self.C = []
        self.D = []
        self.E = []
        self.F = []
        self.G = []
        self.H = []
        self.I = []
        for i in range (9):
            self.A.append(self.s_board[i])
        for i in range (9,18):
            self.B.append(self.s_board[i])
        for i in range (18,27):
            self.C.append(self.s_board[i])
        for i in range (27, 36):
            self.D.append(self.s_board[i])
        for i in range (36, 45):
            self.E.append(self.s_board[i])
        for i in range (45, 54):
            self.F.append(self.s_board[i])
        for i in range (54, 63):
            self.G.append(self.s_board[i])
        for i in range (63, 72):
            self.H.append(self.s_board[i])
        for i in range (72, 81):
            self.I.append(self.s_board[i])
        self.rows_list = [self.A, self.B, self.C, 
                          self.D, self.E, self.F, 
                          self.G, self.H, self.I]             

        #define which indexes belong to which sub grid
        #DO NOT change any of these values
        self.top_left =      [0, 1, 2,  9,10,11,18,19,20]
        self.top_center =    [3, 4, 5, 12,13,14,21,22,23]
        self.top_right =     [6, 7, 8, 15,16,17,24,25,26]
        self.middle_left =   [27,28,29,36,37,38,45,46,47]
        self.middle_center = [30,31,32,39,40,41,48,49,50]
        self.middle_right =  [33,34,35,42,43,44,51,52,53]
        self.bottom_left =   [54,55,56,63,64,65,72,73,74]
        self.bottom_center = [57,58,59,66,67,68,75,76,77]
        self.bottom_right =  [60,61,62,69,70,71,78,79,80]
        self.SQUARES_LIST = [self.top_left, self.top_center, self.top_right, 
                             self.middle_left, self.middle_center, self.middle_right, 
                             self.bottom_left, self.bottom_center, self.bottom_right]

    #populate the board using a url to a .txt file
    #TODO: update domains for each cell based off of
    #initial table data
    def populateBoard(self, file_path, input_type):
        counter = 0        
        if input_type == 1:
            file = urllib.request.urlopen(file_path)
            for line in file:
                decoded_line = line.decode("utf-8")
                for value in decoded_line:
                    if value != " " and value != "\n":
                        self.s_board[counter].setValue(int(value))                   
                        counter+=1
        else:
            file = open(file_path)
            for line in file:                
                for value in line:
                    if value != " " and value != "\n":
                        self.s_board[counter].setValue(int(value))                   
                        counter+=1

    #get all shared cells for cell
    #input, cell object
    #return: list of indexes which are neighbors of the target cell
    #neighbors are in the same row, same column, and same sub grid (square)
    def getNeighbors(self, cell):
        index = cell.getIndex()        
        column = index%9
        row = index/9
        row = int(row)
        neighbors = []

        #get the indexes of all neighboring cells
        for row in self.rows_list:
            if row[column].getIndex() not in neighbors and row[column].getIndex() != index:
                neighbors.append(row[column].getIndex())
            if cell in row:
                for cell in row:
                    if cell.getIndex() not in neighbors and cell.getIndex() != index:
                        neighbors.append(cell.getIndex())
        for square in self.SQUARES_LIST:
            if index in square:
                for cell_index in square:
                    if cell_index not in neighbors and cell_index != index:
                        neighbors.append(cell_index)
        return neighbors

    def getColumnNeighbors(self, cell):
        index = cell.getIndex()        
        column = index%9
        neighbors = []
        for row in self.rows_list:
            if row[column] != cell:
                neighbors.append(row[column])
        return neighbors

    def getRowNeighbors(self, cell):
        neighbors = []
        for row in self.rows_list:
            if cell in row:
                for item in row:
                    if item != cell:
                        neighbors.append(item)
                return neighbors


    def getSquareNeighbors(self, cell):
        neighbors = []
        cell_index = cell.getIndex()
        for square in self.SQUARES_LIST:
            if cell_index in square:
                for index in square:
                    if index != cell_index:
                        neighbors.append(self.s_board[index])
                return neighbors



    #grab all entry values for neighboring cells, return them as a list
    def getNeighborValues (self, neighbors_list):
        values = []
        for index in neighbors_list:
            if self.s_board[index].getValue() not in values and self.s_board[index].getValue() != 0:
                values.append(self.s_board[index].getValue())
        return values

    #iterate through each cell and set domains based off
    #constraint satisfaction, this gets called whenever a domain changes
    def setNewDomains(self):
        for cell in self.s_board:
            neighbors = self.getNeighbors(cell)
            neighbor_values = self.getNeighborValues(neighbors)
            for value in neighbor_values:
                cell.setDomain(value)
                if len(cell.getDomain())==1:
                    #print("Found a value for: ", cell.getIndex())
                    cell.setValue(cell.domain[0])

    def getMostConstrainedVariable(self):
        domain_values = 100
        for cell in self.s_board:
            if cell.getValue() == 0:
                domain = cell.getDomain()
                if domain_values > len(domain):
                    most_constrained_variable = cell
                    domain_values = len(domain)
        if domain_values != 100:
            return most_constrained_variable
        return False
        
    #display function using the list of cells
    #duplicate displays are to test that pointers are
    #working for propogating restraints
    def display(self):
        counter = 0
        for cell in self.s_board:                            
            if counter % 9 == 0:
                if counter!= 0:
                    print ("|")
            if counter % 27 == 0:
                   print ("-------------------------")
            if counter % 3 == 0:
                print ("|", end=" ")     
            print (cell.getValue(), end=" ")         
            counter += 1        
        print ("|\n-------------------------")

    def getCellByIndex(self, index):
        return self.s_board[index]

    def isSolved(self):
        for cell in self.s_board:
            neighbors = self.getNeighborValues(self.getNeighbors(cell))
            if cell.getValue() in neighbors or len(neighbors) < 8:
                return False
        return True



#############################################################################################
#
#TODO: delete everything below this line!
#
##############################################################################################

    #TODO: delete this after testing
    


    #return first cell that matches value
    #TODO: delete this method, used for testing only
    def getCell (self, val):
        for cell in self.s_board:
            if cell.getValue() == val:
                return cell
         
    #display function using the columns 2d array
    #duplicate displays are to test that pointers are
    #working for propogating restraints
    #TODO: delete this method after solution is found
    def displayNeighbors (self):
        counter = 0
        for row in self.rows_list:
            for cell in row:
                if counter % 9 == 0:
                    if counter!= 0:
                        print ("|")
                if counter % 27 == 0:
                   print ("-------------------------")
                if counter % 3 == 0:
                    print ("|", end=" ")
                print (cell.getValue(), end=" ")
                counter+=1
        print ("|\n-------------------------")

    #TODO: delete this method, for testing only
    def displayByIndex(self):
        counter = 0
        for cell in self.s_board:                            
            if counter % 9 == 0:
                if counter!= 0:
                    print ("|")
            if counter % 27 == 0:
                   print ("----------------------------------")
            if counter % 3 == 0:
                print ("|", end=" ")   
            if counter < 10:
                print ("", counter, end=" ")
            else:  
                print (counter, end=" ")         
            counter += 1        
        print ("|\n----------------------------------")
        