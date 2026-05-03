import Manage
import Bank
def Main(User,Args):
    Inventorys = Manage.GetList("Inventorys.json")
    UserId = str(User.id)
    if Args[0].lower() == "fish":
        if UserId not in Inventorys:
            return "You Have No Fish"
        if "Fish" not in Inventorys[UserId]:
            return "You Have No Fish"
        if len(Inventorys[UserId]["Fish"]) == 0: 
            return "You Have No Fish"
        Total = 0
        for Fish in Inventorys[UserId]["Fish"]:
            Total += Fish[1]
        Inventorys[UserId]["Fish"] = []
        Bank.Add(User,Total)
        Manage.UpdateList("Inventorys.json",Inventorys)
        return "Sold All Fish for: **"+ str(Total) + "** Money Coins"
    return "What do you want to sell (Fish)"

