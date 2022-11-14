from ...Game import Game 

def test_empty_board():
    testGame = Game()
    testGame.board.printBoard()
    
    '''assert testGame.board.printBoard == [[".", ".", "."],[".", ".", "."],[".", ".", "."]]'''