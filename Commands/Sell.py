import Manage
import Bank
def Main(User,Args):
    Inventorys = Manage.GetList("Inventorys.json")
    UserId = str(User.id)
    if len(Args) > 0:
        if UserId not in Inventorys:
            return "You Have No "+ Args[0]
        if Args[0] not in Inventorys[UserId]:
            return "You Have No "+ Args[0]
        if len(Inventorys[UserId][Args[0]]) == 0:
            return "You Have No "+ Args[0]
        
        
        Total = 0
        for Item in Inventorys[UserId][Args[0]]:
            Total += Item[1]
        Inventorys[UserId][Args[0]] = []
        Bank.Add(User,Total)
        Manage.UpdateList("Inventorys.json",Inventorys)
        return "Sold All "+Args[0] + " for: **"+ str(Total) + "** Money Coins"



    return "What do you want to sell: " + " | ".join(Inventorys[UserId].keys())

