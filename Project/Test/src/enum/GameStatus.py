from enum import Enum

class GameStatus(Enum):
    Start = 0
    InProgress = 1
    Draw = 2
    FirstPlayerWin = 3
    SecondPlayerWin = 4