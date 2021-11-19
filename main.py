import sudoku, cell

#iterate through every cell and find Naked Doubles
def findNakedDouble(my_sudoku):
    for cell in my_sudoku.s_board:
        nakedDouble = False
        nakedDoubleNeighbors = []
        if not cell.hasValue():
            mcv_domain = cell.getDomain()
            mcv_domain.sort()
            if len(mcv_domain) == 2:
                #first, check for a naked double in this cell's row
                row_neighbors = my_sudoku.getRowNeighbors(cell)
                for neighbor in row_neighbors:
                    neighbor_domain = neighbor.getDomain()
                    neighbor_domain.sort()
                    if neighbor_domain == mcv_domain:
                        for neighbor_cell in row_neighbors:
                            if neighbor_cell != cell and neighbor_cell != neighbor and not neighbor_cell.hasValue():
                                nakedDoubleNeighbors.append(neighbor_cell)
                        if len(nakedDoubleNeighbors)>0:
                            assessNakedDouble(my_sudoku, nakedDoubleNeighbors, mcv_domain)
                            return
                #second, check for a naked double in this cell's column
                column_neighbors = my_sudoku.getColumnNeighbors(cell)
                for neighbor in column_neighbors:
                    neighbor_domain = neighbor.getDomain()
                    neighbor_domain.sort()
                    if neighbor_domain == mcv_domain:
                        for neighbor_cell in column_neighbors:
                            if neighbor_cell != cell and neighbor_cell != neighbor and not neighbor_cell.hasValue():
                                nakedDoubleNeighbors.append(neighbor_cell)
                        if len(nakedDoubleNeighbors)>0:
                            assessNakedDouble(my_sudoku, nakedDoubleNeighbors, mcv_domain)
                            return
                #lastly, check for a naked double in this cell's square
                square_neighbors = my_sudoku.getSquareNeighbors(cell)
                for neighbor in square_neighbors:
                    neighbor_domain = neighbor.getDomain()
                    neighbor_domain.sort()
                    if neighbor_domain == mcv_domain:
                        for neighbor_cell in square_neighbors:
                            if neighbor_cell != cell and neighbor_cell != neighbor and not neighbor_cell.hasValue():
                                nakedDoubleNeighbors.append(neighbor_cell)
                        if len(nakedDoubleNeighbors)>0:
                            assessNakedDouble(my_sudoku, nakedDoubleNeighbors, mcv_domain)
                            return
                

def assessNakedDouble(my_sudoku, neighbors, mcv_domain):

    for neighbor in neighbors:                         
        for value in mcv_domain:
            neighbor_domain = neighbor.getDomain()
            if value in neighbor_domain:
            #if value in my_sudoku.
                if len(neighbor_domain) == 1: 
                    print ("Error is here")    
                neighbor.setDomain(value)
                neighbor_domain = neighbor.getDomain()
                if len(neighbor_domain) == 1:
                    neighbor.setValue(neighbor_domain[0])
                    my_sudoku.setNewDomains()
                    print ("Found a value using Naked Doubles for index:", neighbor.getIndex())
                    return
    return
   


def main():

    my_sudoku = sudoku.Sudoku_Board()
    my_sudoku.display()
    target_url = input("Paste the file domain: ")
    target_url.strip()    
    my_sudoku.populateBoard(target_url)
    print("The sudoku board is:")
    my_sudoku.display()
    print("The indexes are:")
    my_sudoku.displayByIndex()


    #assess new domains after populating the sudoku board
    my_sudoku.setNewDomains()
    mcv = my_sudoku.getMostConstrainedVariable()
    print ("The most constrained variable is at index: ", mcv.getIndex())
    print ("It's possible values are/is: ", mcv.getDomain())
    my_sudoku.display()

    
    #This loop runs the most constrained variable algorithm, help is printed if we run into a wall
    could_not_solve = False
    found_values = 0
    while True:
        mcv = my_sudoku.getMostConstrainedVariable()
        if mcv == False:
            break
        domain = mcv.getDomain()
        if len(domain) == 1:
            mcv.setValue(domain[0])
            my_sudoku.setNewDomains()
            found_values += 1
       
        #TODO: branch to 'findNakedDoubles()' from this check
        #findNakedDoubles() should identify a naked double, solve based off the 
        #constraint and branch back to this loop
        if len(domain) > 1:
            findNakedDouble(my_sudoku)
            #my_sudoku.display()
            #break
       
    my_sudoku.display()

if __name__=='__main__':
    main()