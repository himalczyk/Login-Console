from accounts import CreatePlayer

class Player(CreatePlayer):

    def __init__(self) -> None:
        pass

    def level_up_playerLevel(self, playerLevel):
        #get experienceBar from somewhere
        experienceBar = 0
        if(experienceBar >= 100):
            self.playerLevel = playerLevel +1
        return playerLevel

    def is_playerAlive(self, playerAlive):
        if(self.playerHelth >= 0):
            isPlayerAlive = False
        else:
            isPlayerAlive = True
        return isPlayerAlive