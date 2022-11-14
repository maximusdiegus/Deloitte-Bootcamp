from enum import Enum

class Strings(Enum):
    Menu = "Menu: "
    MenuStartGame = "1. Start new game."
    MenuLoadGame = "2. Load game."
    MenuExitGame = "3. Exit game."
    ExitMessage = "Exiting game. Bye!"
    SelectOption = "Please select an option: "
    ErrorPutSymbol = "Invalid movement. You cannot put a tile in that position."
    WrongOption = "Wrong option. Choose a NUMBER, please"
    
    CreateGameName = "Type the name of your game: "
    CreatePlayer1Name = "Type the name of the 1st player: "
    CreatePlayer2Name = "Type the name of the 2nd player: "
    
    TypeDimensionX = "Type the row number (1 - 3): "    
    TypeDimensionY = "Type the column number (1 - 3): "    
    
    FirstPlayerPlays = "First player plays (x): "
    SecondPlayerPlays = "Second player plays (o): "
    
    FirstPlayerWins = "Congrats! 1st player wins."
    SecondPlayerWins = "Congrats! 2nd player wins."
    
    SaveGameText = "Do you want to save this game? (Y/N) "
    
    ExceptionFileNotSaved = "File could not be saved! :( This is the error: "
    ExceptionFileNotLoaded = "File could not be loaded! :( This is the error: "
    