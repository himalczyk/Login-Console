from accounts import LogIntoTheGame, Register
from startMenu import StartMenu
from game import Room

startMenuChoice = StartMenu.menuChoice()
if startMenuChoice == 'login':
    afterLogin = LogIntoTheGame.getLoginData()
elif startMenuChoice == 'register':
    afterRegister = Register.saveAccountInDB()
elif startMenuChoice == 'exit':
    exit

if(afterLogin):
    Room.enterRoom()
if(afterRegister):
    print('Since you have registered succesfully, you can now login into the game')
    LogIntoTheGame.getLoginData()