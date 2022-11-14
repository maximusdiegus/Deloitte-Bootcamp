from abc import abstractmethod

class IPlayer:
    
    def __init__(self, name, symbol, firstOrSecond):
        self.name = name
        self.symbol = symbol
        self.firstOrSecond = firstOrSecond
    
    @abstractmethod
    def getSymbol(self):
        pass
    
    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod
    def getFirstOrSecondPlayer(self):
        pass