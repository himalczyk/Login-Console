from accounts import CreatePlayer, LogIntoTheGame, Register
from startMenu import StartMenu
from game import Room

startMenuChoice = StartMenu.menuChoice()

if startMenuChoice == 'login':
    afterLogin = LogIntoTheGame.getLoginData()
    CreatePlayer.instantiate_from_csv(str(afterLogin['userName']))
elif startMenuChoice == 'register':
    afterRegister = Register.saveAccountInDB()
elif startMenuChoice == 'exit':
    exit

if(afterLogin):
    print("If you want to start the game. Type 'start'\n")
    print("If you want to go back to the menu. Type 'menu'\n")
    askForAction = input()
    if(askForAction=='start'):
        Room.enterRoom()
    elif(askForAction=='menu'):
        startMenuChoice
if(afterRegister):
    print('Since you have registered succesfully, you can now login into the game')
    LogIntoTheGame.getLoginData()