from Board import Board

def test_empty_board():
    testBoard = Board(3,3)
    assert testBoard == [[".", ".", "."],[".", ".", "."],[".", ".", "."]]

def test_insert_board():
    testBoard = Board(3,3)
    testBoard.putSymbol(0, 0, "x")
    assert testBoard == [["x", ".", "."],[".", ".", "."],[".", ".", "."]]

def test_insert_board2():
    testBoard = Board(3,3)
    testBoard.putSymbol(2, 2, "x")
    assert testBoard == [[".", ".", "."],[".", ".", "."],[".", ".", "x"]]

def test_insert_board3():
    testBoard = Board(3,3)
    testBoard.putSymbol(1, 2, "o")
    assert testBoard == [[".", ".", "."],[".", ".", "o"],[".", ".", "o"]]

def test_row_wins():
    testBoard = Board(3,3)
    testBoard.putSymbol(0, 0, "x")
    testBoard.putSymbol(0, 1, "x")
    testBoard.putSymbol(0, 2, "x")
    assert testBoard == [["x", "x", "x"],[".", ".", "."],[".", ".", "."]] 
    assert testBoard.end == True

def test_column_wins():
    testBoard = Board(3,3)
    testBoard.putSymbol(0, 1, "o")
    testBoard.putSymbol(1, 1, "o")
    testBoard.putSymbol(2, 1, "o")
    assert testBoard == [[".", "o", "."],[".", "o", "."],[".", "o", "."]]
    assert testBoard.end == True

def test_diagonal_wins():
    testBoard = Board(3,3)
    testBoard.putSymbol(0, 0, "x")
    testBoard.putSymbol(0, 1, "x")
    testBoard.putSymbol(0, 2, "x")
    assert testBoard == [["x", ".", "."],[".", "x", "."],[".", ".", "x"]]
    assert testBoard.end == True

def test_reverse_diagonal_wins():
    testBoard = Board(3,3)
    testBoard.putSymbol(0, 0, "o")
    testBoard.putSymbol(0, 1, "o")
    testBoard.putSymbol(0, 2, "o")
    assert testBoard == [[".", ".", "o"],[".", "o", "."],["o", ".", "."]]
    assert testBoard.end == True
    
def test_random_symbols():
    testBoard = Board(3,3)
    testBoard.putSymbol(0, 0, "o")
    testBoard.putSymbol(0, 2, "x")
    testBoard.putSymbol(1, 2, "o")
    testBoard.putSymbol(2, 2, "x")
    testBoard.putSymbol(0, 1, "o")
    assert testBoard == [["o", "o", "x"],[".", ".", "o"],[".", ".", "x"]]
    assert testBoard.end == False