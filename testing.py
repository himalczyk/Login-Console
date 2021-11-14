from accounts import CreatePlayer    
import csv
    
def instantiate_from_csv(userName: str):
    with open('accounts.csv', 'r+') as getPlayer:
        reader = csv.reader(getPlayer, delimiter=' ', quotechar='|')
        for line in reader:
            print(line)
            for cell in line:
                print(cell)
                if(userName in cell):
                    player = CreatePlayer(
                        playerName=userName
                    )
                    print(player.playerName)
                    break
    return player