from accounts import LogIntoTheGame, Register
from startMenu import StartMenu

startMenuChoice = StartMenu.menuChoice()
if startMenuChoice == 'login':
    LogIntoTheGame.getLoginData()
elif startMenuChoice == 'register':
    Register.saveAccountInDB()