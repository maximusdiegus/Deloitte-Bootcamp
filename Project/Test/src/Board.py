from array import *
from Enum.Symbol import Symbol

class Board:
   
    def __init__(self, dimX, dimY):
        self.dimX = dimX
        self.dimY = dimY
        self.board = [[Symbol.Dot.value for i in range(self.dimX)] for i in range(self.dimY)]
    
    def putSymbol(self, posX, posY, symbol):
        if posX < 0 or posX > self.dimX or posY < 0 or posY > self.dimY:
            return False
        elif self.board[posX][posY] == Symbol.Dot.value:
            self.board[posX][posY] = symbol
            return True
        else:
            return False

        
                
    def checkWin(self, symbol):
        match = True
        
        '''Check Row'''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != symbol:
                    match = False
            if match == True:
                return True
            else:
                match = True
            
        if match == False:
            match = True
                          
        '''Check Column'''
        columnArray = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                columnArray.append(self.board[j][i])
                match = all(ele == symbol for ele in columnArray)
                
            if match == True:
                return True
            else:
                match = True    
        
        if match == False:
            match = True
        
        '''Check Diagonal'''
        diagonalArray = []
        for i in range(len(self.board)):
            diagonalArray.append(self.board[i][i])
            match = all(ele == symbol for ele in diagonalArray)
            if match == True:
                return True
            else:
                match = True
        
        '''Check Diagonal Backwards'''
        j = 0
        k = len(self.board) -1
        diagonalArray = []
        
        for i in range(len(self.board)):
            diagonalArray.append(self.board[j][k])
            j += 1
            k -= 1
        match = all(ele == symbol for ele in diagonalArray)
        
        if match:
            return True
        else:
            return False
            
    
    def printBoard(self):
        for i in range(len(self.board)):
            print("| ", end="")
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print("|")

# testBoard = Board(3,3)
# print(testBoard.putSymbol(0, 0, "x"))
# print(testBoard.putSymbol(0, 1, "x"))
# print(testBoard.putSymbol(0, 2, "x"))
# print(testBoard.putSymbol(0, 2, "x"))
# testBoard.printBoard()
