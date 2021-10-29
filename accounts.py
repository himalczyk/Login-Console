import csv
        
class Register():

    accountsBasePlaceholder = {}

    def __init__(self, userName, password, email):
        self.userName = userName
        self.password = password
        self.email = email

        Register.accountsBasePlaceholder['userName'] = self.userName
        Register.accountsBasePlaceholder['password'] = self.password
        Register.accountsBasePlaceholder['email'] = self.email

    def saveAccountInDB():
        askForUserName = input("Please provide your userName: \n")
        askForPassword = input("Please provide you password: \n")
        askForEmail = input("Please provide your email: \n")
        playerDetails = CreatePlayer.instantiate_player_to_csv()

        Register(
            userName = askForUserName,
            password = askForPassword,
            email = askForEmail,
        )
        Register.accountsBasePlaceholder['playerName'] = playerDetails['playerName']
        Register.accountsBasePlaceholder['playerLevel'] = playerDetails['playerLevel']
        Register.accountsBasePlaceholder['playerAlive'] = playerDetails['playerAlive']
        Register.accountsBasePlaceholder['playerExperience'] = playerDetails['playerExperience']
        Register.accountsBasePlaceholder['playerHealth'] = playerDetails['playerHealth']

        with open ('accounts.csv', 'a+') as accountsFile:
            accountsFile.read()
            for value in Register.accountsBasePlaceholder.values():
                    accountsFile.write(str(value))
                    accountsFile.write(",")
            accountsFile.write("\n")
        Register.accountsBasePlaceholder.clear()
    
class LogIntoTheGame(): #Register ?

    def getLoginData():
        provideUsername = input("Username: \n")
        providePassword = input("Password: \n")

        loggedInUser = {}
        loggedInUser['userName'] = provideUsername

        with open ('accounts.csv', 'r+') as checkDataAccountsFile:
            reader = csv.reader(checkDataAccountsFile, delimiter=' ', quotechar='|')
            for line in reader:
                for value in line:
                    if(provideUsername and providePassword in value):
                        break
        print("Logged in succesfully")
        return loggedInUser

class CreatePlayer():
    writeToFilePlayerPlaceholder = {}
    def __init__(self, playerName = str, playerLevel = 1, playerAlive = True, playerExperience = 0, playerHealth=100):
        
        self.playerName = playerName
        self.playerLevel = playerLevel
        self.playerAlive = playerAlive
        self.playerExperience = playerExperience
        self.playerHealth = playerHealth

        CreatePlayer.writeToFilePlayerPlaceholder["playerName"] = self.playerName
        CreatePlayer.writeToFilePlayerPlaceholder["playerLevel"] = self.playerLevel
        CreatePlayer.writeToFilePlayerPlaceholder["playerAlive"] = self.playerAlive
        CreatePlayer.writeToFilePlayerPlaceholder["playerExperience"] = self.playerExperience
        CreatePlayer.writeToFilePlayerPlaceholder["playerHealth"] = self.playerHealth
        
    @classmethod
    def instantiate_player_to_csv(cls):
        askForPlayerName = input("Please type the name of your character:\n")
        CreatePlayer(
            playerName = askForPlayerName,
        )
        return CreatePlayer.writeToFilePlayerPlaceholder