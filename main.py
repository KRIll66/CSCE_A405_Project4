import sudoku, cell

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

    #############################################################################
    #The below commented out code was used to verify that neighboring cells are
    #being assessed correctly and the domains are being assessed correctly
    #############################################################################

    #target_index = input("Enter the target cell by index:")
    #cell = my_sudoku.getCellByIndex(int(target_index))
    #neighbors = my_sudoku.getNeighbors(cell)
    
    #print("The current value at that cell is: ",cell.getValue())
    #print("The neighbors are at indexes: ", neighbors)
    #print("The taken values are: ", sorted(my_sudoku.getNeighborValues(neighbors)))

    #assess new domains after populating the sudoku board
    my_sudoku.setNewDomains()
    mcv = my_sudoku.getMostConstrainedVariable()
    print ("The most constrained variable is at index: ", mcv.getIndex())
    print ("It's possible values are/is: ", mcv.getDomain())
    my_sudoku.display()

    #This loop runs the most constrained variable algorithm, help is printed if we run into a wall
    while True:
        mcv = my_sudoku.getMostConstrainedVariable()
        if mcv == False:
            break
        domain = mcv.getDomain()
        if len(domain) <= 1:
            mcv.setValue(domain[0])
            my_sudoku.setNewDomains()
        my_sudoku.display()
        if len(domain) > 1:
            print ("Help")

if __name__=='__main__':
    main()