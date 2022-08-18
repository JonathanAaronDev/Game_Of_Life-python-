from cell import *


class Game:
    def __init__(self):
        self.matrix = newmatrix()
        self.listOfAliveCells = []
        self.size = 8


def newmatrix():
        matrix = [[], [], [], [], [], [], [], []]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i].append(Cell(i, j, False, 0))
        return matrix




def checkForNeighbor(matrix, listOfAliveCells):
        # Run all over the alive cells and chcek for alive Neighbors
        for j in range(len(listOfAliveCells)):
            row = listOfAliveCells[j][0]
            column = listOfAliveCells[j][1] - 1
            ##print("alive cell at position" + "[" + str(row) + "]" + "[" + str(listOfAliveCells[j][1]) + "]")
            # Run all over the upper row and add counter++ because he has a Neighbor.
            for k in range(3):
                if ((row - 1 < 0) or (row + 1 > 7) or (column + k > 7)):
                    break
                if ((column + k < 0)):
                    continue
                matrix[row - 1][column + k].counterADD()
            # Run all over the lower row and add counter++ because he has a Neighbor.
            for t in range(3):
                if ((row - 1 < 0) or (row + 1 > 7) or (column + t > 7)):
                    break
                if ((column + t < 0)):
                    continue
                matrix[row + 1][column + t].counterADD()
            # Run over the current row and add counter++ because he has a Neighbor.
            for q in range(3):
                if ((row - 1 < 0) or (row + 1 > 7) or (column + q > 7)):
                    break
                elif ((column + q < 0) or (column + q == listOfAliveCells[j][1])):
                    continue
                matrix[row][column + q].counterADD()

        print("end of checkForNeighbor function")
        return matrix


def update(matrix, listOfAliveCells):
        # Build New Matrix for work
        matrixNew = newmatrix()
        # varible of new list of alive for work
        listOfAliveCellsNEW = []
        # check every cell in the list of alive cell and determine if he will be alive or dead
        for j in range(len(listOfAliveCells)):
            row = listOfAliveCells[j][0]
            column = listOfAliveCells[j][1] - 1
            # Check the Lower row and update state
            for k in range(3):

                # Sanity test
                if ((row - 1 < 0) or (row + 1 > 7) or (column + k > 7)):
                    break
                if ((column + k < 0)):
                    continue
                # varible for work
                celllorow = matrix[row - 1][column + k]
                # Update stage
                if ((celllorow.counter == 2 and celllorow.state == True) or (celllorow.counter == 3)):
                    list_search = [row - 1, column + k]
                    if list_search in listOfAliveCellsNEW:
                        continue
                    else:
                        matrixNew[row - 1][column + k].state = True
                        listOfAliveCellsNEW.append(list_search)
                    ##print("matrix at position " + "[" + str(row - 1) + "]" + "[" + str(column + k) + "]" + "is alive")
                elif ((celllorow.counter <= 1) or (celllorow.counter > 3 and celllorow.state == True)):
                    matrixNew[row - 1][column + k].state = False
            # Check the Upper row and update state
            for t in range(3):
                # Sanity test
                if (row - 1 < 0) or (row + 1 > 7) or (column + t > 7):
                    break
                if column + t < 0:
                    continue
                # varible for work
                celluprow = matrix[row + 1][column + t]
                # Update stage
                if ((celluprow.counter == 2 and celluprow.state == True) or (celluprow.counter == 3)):
                    ##matrixNew[row+1][column+t].state=True
                    ##listOfAliveCellsNEW.append([row+1,column+t])
                    list_search = [row + 1, column + t]
                    if list_search in listOfAliveCellsNEW:
                        continue
                    else:
                        matrixNew[row + 1][column + t].state = True
                        listOfAliveCellsNEW.append(list_search)
                    ##print("matrix at position " + "[" + str(row + 1) + "]" + "[" + str(column + t) + "]" + "is alive")
                elif ((celluprow.counter <= 1) or (celluprow.counter > 3 and celluprow.state == True)):
                    matrixNew[row + 1][column + t].state = False
            # Check the current row and update state
            for q in range(3):
                # Sanity test
                if ((row - 1 < 0) or (row + 1 > 7) or (column + q > 7)):
                    break
                if (column + q < 0):
                    continue
                # varible for work
                cellcurrentrow = matrix[row][column + q]
                # Update stage
                if ((cellcurrentrow.counter == 2 and cellcurrentrow.state == True) or (cellcurrentrow.counter == 3)):
                    # matrixNew[row][column+q].state=True
                    # listOfAliveCellsNEW.append([row,column+q])
                    list_search = [row, column + q]
                    if list_search in listOfAliveCellsNEW:
                        continue
                    else:
                        matrixNew[row][column + q].state = True
                        listOfAliveCellsNEW.append(list_search)
                    ##print("matrix at position " + "[" + str(row) + "]" + "[" + str(column + q) + "]" + "is alive")
                elif ((cellcurrentrow.counter <= 1) or (cellcurrentrow.counter > 3 and cellcurrentrow.state == True)):
                    matrixNew[row][column + q].state = False
        # update the old matrix and the old list
        print("end of Update function")
        return (matrixNew, listOfAliveCellsNEW)
