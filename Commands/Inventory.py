import Manage


def InvenString(Id):
    
    ReturningString = ""
    Inventorys = Manage.GetList("Inventorys.json")
    if Id in Inventorys:
        if "fish" in Inventorys[Id]:
            if len(Inventorys[Id]["fish"]) != 0:
                ReturningString = ReturningString + "## __Fih__ \n"
                fishieList = {}
                for fishie in Inventorys[Id]["fish"]:
                    if fishie[0] in fishieList:
                        fishieList[fishie[0]] = fishieList[fishie[0]] + 1 
                    else:
                        fishieList[fishie[0]] = 1
                fishieItems = [*fishieList.items()]
                for fishieTuple in fishieItems:
                    ReturningString = ReturningString + "" + fishieTuple[0] + " : " +str(fishieTuple[1]) + "\n"
        for Type in Inventorys[Id]:
            if Type != "fish":

                if len(Inventorys[Id][Type]) != 0:

                    ReturningString = ReturningString + "## __"+Type+"s__\n"
                    List = {}
                    for Item in Inventorys[Id][Type]:
                        if Item[0] in List:
                            List[Item[0]] = List[Item[0]] + 1
                        else:
                            List[Item[0]] = 1
                    ListItems = [*List.items()]
                    for Tuple in ListItems:
                        ReturningString = ReturningString + "" + Tuple[0] + " : " +str(Tuple[1]) + "\n"

                    
        return ReturningString
    return "Nothing"



def Main(User,Args):
    Id = str(User.id)
    if len(Args) == 0:
        return InvenString(Id)
    else:
        
        print(Args[0][2:-1])
        if Args[0][0:2] == "<@" and Args[0][len(Args[0])-1]:
            return InvenString(Args[0][2:-1])
        else:
            return "Please @ somebody to see their inventory"
    


def Add(User,Item,Type):
    Inventorys = Manage.GetList("Inventorys.json")
    Id = str(User.id)
    if Id in Inventorys:
        if Type in Inventorys[Id]:
            Inventorys[Id][Type].append(Item)
        else:
            Inventorys[Id][Type] = [Item] 
    else:
        Inventorys[Id] = {}
        Inventorys[Id][Type] = [Item]
    Manage.UpdateList("Inventorys.json",Inventorys)
    
