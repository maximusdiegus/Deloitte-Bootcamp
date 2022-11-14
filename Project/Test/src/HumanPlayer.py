from IPlayer import IPlayer

class HumanPlayer(IPlayer):
    
    def __init__(self):
        super().__init__()
    
    def getSymbol(self):
        return self.symbol
    
    def getName(self):
        return self.name
    
    def getFirstOrSecondPlayer(self):
        return self.firstOrSecond