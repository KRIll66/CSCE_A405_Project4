import sudoku, cell

#iterate through every cell and find Naked Doubles
def findNakedDouble(my_sudoku):
    found_value = False
    for cell in my_sudoku.s_board:        
        nakedDoubleNeighbors = []
        if not cell.hasValue():
            double_domain = cell.getDomain()
            double_domain.sort()
            if len(double_domain) == 2:

                #first, check for a naked double in this cell's row
                row_neighbors = my_sudoku.getRowNeighbors(cell)
                for neighbor in row_neighbors:
                    neighbor_domain = neighbor.getDomain()
                    neighbor_domain.sort()
                    if neighbor_domain == double_domain:
                        nakedDoubleNeighbors.append(cell)
                        nakedDoubleNeighbors.append(neighbor)
                if len(nakedDoubleNeighbors)>0:                   
                    found_value = assessNaked(my_sudoku, nakedDoubleNeighbors, row_neighbors, double_domain)
                   
                          
                #second, check for a naked double in this cell's column
                column_neighbors = my_sudoku.getColumnNeighbors(cell)
                nakedDoubleNeighbors = []
                for neighbor in column_neighbors:
                    neighbor_domain = neighbor.getDomain()
                    neighbor_domain.sort()
                    if neighbor_domain == double_domain:
                        nakedDoubleNeighbors.append(cell)
                        nakedDoubleNeighbors.append(neighbor)
                if len(nakedDoubleNeighbors)>0:
                    found_value = assessNaked(my_sudoku, nakedDoubleNeighbors, column_neighbors, double_domain)
                            

                #lastly, check for a naked double in this cell's square
                square_neighbors = my_sudoku.getSquareNeighbors(cell)
                nakedDoubleNeighbors = []
                for neighbor in square_neighbors:
                    neighbor_domain = neighbor.getDomain()
                    neighbor_domain.sort()
                    if neighbor_domain == double_domain:
                        nakedDoubleNeighbors.append(cell)
                        nakedDoubleNeighbors.append(neighbor)
                if len(nakedDoubleNeighbors)>0:
                    found_value = assessNaked(my_sudoku, nakedDoubleNeighbors, square_neighbors, double_domain)
                            
    return found_value

def findNakedTriple(my_sudoku):
    found_value = False
    for cell in my_sudoku.s_board: 
        if cell.getIndex() == 10:
            x = 10
            pass       
        naked_triple_neighbors = []
        naked_triple_domain = []
        test_domain = []
        if not cell.hasValue():
            triple_domain = cell.getDomain()
            triple_domain.sort()

            #can only have a naked triple if domain is 3 or less
            if len(triple_domain) <= 3:
                for value in triple_domain:
                    naked_triple_domain.append(value)
                    test_domain.append(value)
                naked_triple_neighbors.append(cell)

                #first, check for a naked triple in this cell's row
                row_neighbors = my_sudoku.getRowNeighbors(cell)
                for neighbor in row_neighbors:
                    if not neighbor.hasValue():
                        neighbor_domain = neighbor.getDomain()                    
                        neighbor_domain.sort()

                        #if the domain is greater than three then it can't be a naked triple
                        #check for any duplicate values, the target is a list of 3 values shared across 3 cell domains
                        if len(neighbor_domain) <= 3:
                            for value in neighbor_domain:
                                if value not in naked_triple_domain:
                                    test_domain.append(value)
                                    
                        #we have gone over value, this cell is not a triple candidate
                        #remove it's domain from the list and move on to the next neighbor
                        #otherwise, scribe it to our working triple_domain list
                            if len(test_domain) > 3:
                                for value in neighbor_domain:
                                    if value not in naked_triple_domain:
                                        test_domain.remove(value)
                            else:
                                for value in test_domain:
                                    if value not in naked_triple_domain:
                                        naked_triple_domain.append(value)
                                naked_triple_neighbors.append(neighbor)
                                if len(naked_triple_neighbors) == 3:
                                    print("Found naked Triple using rows!!!")
                                    for friend in naked_triple_neighbors:
                                        print("Cell at index: ", friend.getIndex(), "with domain of: ", friend.getDomain())
                                    found_value = assessNaked(my_sudoku, naked_triple_neighbors, row_neighbors, naked_triple_domain)
                                    #break
                                    if found_value:
                                        my_sudoku.displayByIndex()
                                        my_sudoku.display()
                                        
                #second, check for a naked triple in this cell's column
                naked_triple_neighbors=[]
                naked_triple_neighbors.append(cell)
                column_neighbors = my_sudoku.getColumnNeighbors(cell)
                for neighbor in column_neighbors:
                    if not neighbor.hasValue():
                        neighbor_domain = neighbor.getDomain()                    
                        neighbor_domain.sort()

                        #if the domain is greater than three then it can't be a naked triple
                        #check for any duplicate values, the target is a list of 3 values shared across 3 cell domains
                        if len(neighbor_domain) <= 3:
                            for value in neighbor_domain:
                                if value not in naked_triple_domain:
                                    test_domain.append(value)
                                    
                        #we have gone over value, this cell is not a triple candidate
                        #remove it's domain from the list and move on to the next neighbor
                        #otherwise, scribe it to our working triple_domain list
                            if len(test_domain) > 3:
                                for value in neighbor_domain:
                                    if value not in naked_triple_domain:
                                        test_domain.remove(value)
                            else:
                                for value in test_domain:
                                    if value not in naked_triple_domain:
                                        naked_triple_domain.append(value)
                                naked_triple_neighbors.append(neighbor)
                                if len(naked_triple_neighbors) == 3:
                                    print("Found naked Triple using columns!!!")
                                    for friend in naked_triple_neighbors:
                                        print("Cell at index: ", friend.getIndex(), "with domain of: ", friend.getDomain())
                                    found_value = assessNaked(my_sudoku, naked_triple_neighbors, column_neighbors, naked_triple_domain)
                                    #break
                                    if found_value:
                                        my_sudoku.displayByIndex()
                                        my_sudoku.display()

                #last, check for a naked triple in this cell's square
                naked_triple_neighbors = []
                naked_triple_neighbors.append(cell)
                square_neighbors = my_sudoku.getSquareNeighbors(cell)
                for neighbor in square_neighbors:
                    if not neighbor.hasValue():
                        neighbor_domain = neighbor.getDomain()                    
                        neighbor_domain.sort()

                        #if the domain is greater than three then it can't be a naked triple
                        #check for any duplicate values, the target is a list of 3 values shared across 3 cell domains
                        if len(neighbor_domain) <= 3:
                            for value in neighbor_domain:
                                if value not in naked_triple_domain:
                                    test_domain.append(value)
                                    
                        #we have gone over value, this cell is not a triple candidate
                        #remove it's domain from the list and move on to the next neighbor
                        #otherwise, scribe it to our working triple_domain list
                            if len(test_domain) > 3:
                                for value in neighbor_domain:
                                    if value not in naked_triple_domain:
                                        test_domain.remove(value)
                            else:
                                for value in test_domain:
                                    if value not in naked_triple_domain:
                                        naked_triple_domain.append(value)
                                naked_triple_neighbors.append(neighbor)
                                if len(naked_triple_neighbors) == 3:
                                    print("Found naked Triple using squares!!!")
                                    for friend in naked_triple_neighbors:
                                        print("Cell at index: ", friend.getIndex(), "with domain of: ", friend.getDomain())
                                    found_value = assessNaked(my_sudoku, naked_triple_neighbors, square_neighbors, naked_triple_domain)
                                    #break
                                    if found_value:
                                        my_sudoku.displayByIndex()
                                        my_sudoku.display()

    return found_value
                                    

                
                

#when a naked double has been found, update the neighboring domains
def assessNaked(my_sudoku, friends, neighbors, domain):

    found_value = False

    for neighbor in neighbors:  
        #iterate through each value in the naked domain
        #only if we are not in a bound pair/triplet cell
        if neighbor not in friends:
            for value in domain:
                neighbor_domain = neighbor.getDomain()
                if value in neighbor_domain:           
                    if len(neighbor_domain) == 1: 
                        print ("Error is here")   
                    #remove the value from the neighbors domain 
                    neighbor.setDomain(value)
                    neighbor_domain = neighbor.getDomain()
                    if len(neighbor_domain) == 1:
                        neighbor.setValue(neighbor_domain[0])
                        my_sudoku.setNewDomains()
                        if len(domain) == 2:
                            print ("Found a value using Naked Doubles for index:", neighbor.getIndex())
                        if len(domain) == 3:
                            print ("Found a value using Naked Triples!!!!! for index:", neighbor.getIndex())                        
                        found_value = True
    return found_value
   


def main():
    my_sudoku = sudoku.Sudoku_Board()

    #get user input for file location
    while True:
        input_type = input("To use a .txt from a web domain, press 1;\nTo use a .txt from a local directory, press 2;\n")    
        try:
            input_type = int(input_type)
            if input_type == 1:
                file_path = input("Paste the file domain:\n")
                break
            if input_type == 2:
                file_path = input("Paste the file path:\n")
                break
            if input_type > 2 or input_type < 1:
                print ("Your input is out of range...")
        except:
            print("The input must be an integer...")
        
    file_path.strip()    
    my_sudoku.populateBoard(file_path, int(input_type))
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

      
    
    duplicate_loops = 0
    while True:
        found_a_value = False
        mcv = my_sudoku.getMostConstrainedVariable()
        if mcv == False:
            break
        domain = mcv.getDomain()
        if len(domain) == 1:
            mcv.setValue(domain[0])
            my_sudoku.setNewDomains()
            print ("Found a value using Constraint Satisfaction for index:", mcv.getIndex())
            found_a_value = True
                 
       
        if len(domain) == 2:
            found_a_value = findNakedDouble(my_sudoku)
            my_sudoku.setNewDomains()
            #my_sudoku.display()
            #break
        
        #naked doubles wasn't able to solve the issue, try naked triples
        if not found_a_value:
            my_sudoku.display()
            found_a_value = findNakedTriple(my_sudoku)
            my_sudoku.setNewDomains()
        
        
    my_sudoku.display()

if __name__=='__main__':
    main()