from Enum.GameStatus import GameStatus
from Enum.Symbol import Symbol
from Enum.Strings import Strings
from Board import Board
from IPlayer import IPlayer
import json


class Game:
        
    def __init__ (self):
        self.board = Board(3,3)
        self.firstPlayer = IPlayer("Player1", Symbol.Cross, 1)
        self.secondPlayer = IPlayer("Player2", Symbol.Circle, 2)
        self.playerTurn = 1
        self.gameStatus = GameStatus.Start.value
        self.gameName = ""
        
        
        
    def menu(self):
        ans = True
        while ans:
            print("-----------------------")
            print("| " + Strings.Menu.value + " |".rjust(15," "))
            print("| "+ "-------------------" + " |")
            print("|  " + Strings.MenuStartGame.value + " |")
            print("|  " + Strings.MenuLoadGame.value + " |".rjust(7," "))
            print("|  " + Strings.MenuExitGame.value + " |".rjust(7," "))
            print("-----------------------")
            print(Strings.SelectOption.value)
            
            inp = input()
            
            if inp == "1":
                self.gameName = input(Strings.CreateGameName.value) 
                self.firstPlayer.name = input(Strings.CreatePlayer1Name.value)
                self.secondPlayer.name = input(Strings.CreatePlayer2Name.value)
                self.gameStatus = GameStatus.InProgress.value
                
                while self.gameStatus == GameStatus.InProgress.value:
                    self.board.printBoard()
                    x = int(input(Strings.TypeDimensionX.value)) - 1
                    y = int(input(Strings.TypeDimensionY.value)) - 1
                    if self.playerTurn == 1:
                        player = self.firstPlayer
                        print(Strings.FirstPlayerPlays.value)
                    else:
                        player = self.secondPlayer
                        print(Strings.FirstPlayerPlays.value)
                    
                    self.play(x, y, player)
                    self.playerTurn = 2
                
                ans = input(Strings.SaveGameText.value)
                if ans == "Y":
                    self.saveGame(self.gameName)
                
            elif inp == "2":
                self.gameName = input(Strings.CreateGameName.value)
            elif inp == "3":
                print(Strings.ExitMessage.value)
                ans = False
            else:
                print(Strings.WrongOption.value)
          
        
    def play(self, dimX, dimY, player):
        symbol = player.symbol
        notErrorMove = False
        
        while notErrorMove == False:
            notErrorMove = self.board.putSymbol(dimX, dimY, symbol.value)
            if notErrorMove == False:
                Strings.ErrorPutSymbol.value
                
        checkWin = self.board.checkWin(symbol)
        
        if checkWin == True:
            self.showWinMessage(player)
            if player.firsOrSecond == 1:
                self.gameStatus = GameStatus.FirstPlayerWin
            else:
                self.gameStatus = GameStatus.SecondPlayerWin

    def printCurrentBoard(self):
        self.board.printBoard()
    
    def setGameStatus(self, gameStatus):
        self.gameStatus = gameStatus
    
    def getGameStatus(self):
        return (self.gameStatus)
    
    def showWinMessage(self, player):
        if player.getFirstOrSecondPlayer() == 1:
            print(Strings.FirstPlayerWins.value)
        else:
            print(Strings.SecondPlayerWins.value)
    
    def setPlayerTurn(self, playerTurn):
        self.playerTurn = playerTurn
    
    def getPlayerTurn(self):
        return (self.playerTurn)
    
    def saveGame(self, name):
        
        try:
            
            file = open(name + ".json", "w")
            
            infoToSave = {
                "gameName": name,
                "Player1": self.firstPlayer.getName(),
                "Player2": self.secondPlayer.getName(),
                "BoardStatus": self.board.board,
                "GameStatus": self.getGameStatus(),
                "Turn": self.getPlayerTurn()
            }
            
            json.dump(infoToSave, file, indent = 1)
            file.close()
            
        except Exception as e:
            print(Strings.ExceptionFileNotSaved)
            print(e)
    
        
    def loadGame(self, name):
        try:
            file = open(name + '.json')
            data = json.loads(file)
            
            self.game = data["gameName"]
            self.firstPlayer.name = data["Player1"]
            self.secondPlayer.name = data["player2"]
            self.board = data["BoardStatus"]
            self.setGameStatus(data["GameStatus"]) 
            self.setPlayerTurn(data["BoardStatus"]) 
            
        except Exception as e:
            print(Strings.ExceptionFileNotLoaded)
            print(e)
        
        
testGame = Game()
testGame.menu()