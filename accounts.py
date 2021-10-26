import csv

class CreatePlayer():
    writeToFilePlayerPlaceholder = {}
    def __init__(self, playerName = str, playerLevel = 1, playerAlive = True, playerExperience = 0, playerHealth=100):

        self.playerName = playerName
        self.playerLevel = playerLevel
        self.playerAlive = playerAlive
        self.playerExperience = playerExperience
        self.playerHelth = playerHealth

        CreatePlayer.writeToFilePlayerPlaceholder["playerName"] = self.playerName
        CreatePlayer.writeToFilePlayerPlaceholder["playerLevel"] = self.playerLevel
        CreatePlayer.writeToFilePlayerPlaceholder["playerAlive"] = self.playerAlive
        CreatePlayer.writeToFilePlayerPlaceholder["playerExperience"] = self.playerExperience

    @classmethod
    def instantiate_player_to_csv(cls):
        askForPlayerName = input("Please type the name of your character:\n")
        CreatePlayer(
            playerName = askForPlayerName,
        )
        with open ('players.csv', 'a+') as playersFile:
            playersFile.read()
            for value in CreatePlayer.writeToFilePlayerPlaceholder.values():
                playersFile.write(str(value))
                playersFile.write("\t")
            playersFile.write("\n")
        CreatePlayer.writeToFilePlayerPlaceholder.clear()
        
class Register():

    accountsBasePlaceholder = {}

    def __init__(self, userName, password, email):
        self.userName = userName
        self.password = password
        self.email = email

        Register.accountsBasePlaceholder['userName'] = self.userName
        Register.accountsBasePlaceholder['password'] = self.password
        Register.accountsBasePlaceholder['email'] = self.email

    @classmethod
    def saveAccountInDB(cls):
        askForUserName = input("Please provide your userName: \n")
        askForPassword = input("Please provide you password: \n")
        askForEmail = input("Please provide your email: \n")

        Register(
            userName = askForUserName,
            password = askForPassword,
            email = askForEmail
        )
        with open ('accounts.csv', 'a+') as accountsFile:
            accountsFile.read()
            for value in Register.accountsBasePlaceholder.values():
                    accountsFile.write(str(value))
                    accountsFile.write(",")
            accountsFile.write("\n")
        Register.accountsBasePlaceholder.clear()

class ReadPlayerFromDB(Register):

    def __init__(self) -> None:
        pass

    def getLoggedInPlayer(self, userName, password):
        pass
    
class LogIntoTheGame(Register):

    def getLoginData():
        provideUsername = input("Username: \n")
        providePassword = input("Password: \n")

        with open ('accounts.csv', 'r+') as checkData:
            reader = csv.reader(checkData, delimiter=' ', quotechar='|')
            for line in reader:
                for value in line:
                    if(provideUsername and providePassword in value):
                        break
        print("Logged in succesfully")

LogIntoTheGame.getLoginData()