import Manage
Exploring = Manage.GetList("Exploring.json")
ExploringPlayers = Manage.GetList("ExploringPlayers.json")
import time
import Inventory
import random
print(Exploring )
Locations = Exploring.keys()
def Main(User,Args):
    if len(Args) < 1:
        return "Please Provide One Argument"
    else:
        if Args[0].lower() not in Locations:
            return "Please enter one of these locations: " +"|".join(Locations)
        else:
            if str(User.id) not in ExploringPlayers:
                ExploringPlayers[str(User.id)] = 0
            if time.time() - ExploringPlayers[str(User.id)] < 3600: 
                return "You can only explore once an hour"
            else:
                CanGet = Exploring[Args[0].lower()]
                
                Total = 0
                for Item in CanGet:
                    print(Item)
                    Total += Item[2]
                
                RandomWeight = random.randint(0,Total)
                Total = 0
                Found = False
                PickedItemNum = -1
                for Item in CanGet:
                    if (Total == RandomWeight or RandomWeight < Total) and Found == False:
                        Found = True
                        PickedItemNum += 1
                PickedItem = CanGet[PickedItemNum]
                ExploringPlayers[str(User.id)] = time.time()
                Manage.UpdateList("ExploringPlayers.json",ExploringPlayers)
                Inventory.Add(User,PickedItem[0],PickedItem[1])
                return User.mention + "Got: **" +PickedItem[0][0]+ "**"
        

#Base = [Item,Type,Rarity]
#Item = [Name,Value]
            
                




    
