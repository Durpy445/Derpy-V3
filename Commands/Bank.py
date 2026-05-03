import Manage
def Main(User,Args):
    Bank = Manage.GetList("Bank.json")
    UserId = str(User.id)
    if UserId not in Bank:
        return "Broke Bih"
    MoneyCoins = Bank[UserId]
    return User.mention + " has: **" + str(MoneyCoins) + "** Money Coins"

def Add(User,Amount):
    Bank = Manage.GetList("Bank.json")
    UserId = str(User.id)
    if UserId not in Bank:
        Bank[UserId] = int(Amount)
        Manage.UpdateList("Bank.json",Bank)
        return
    Bank[UserId] = Bank[UserId]+int(Amount)
    Manage.UpdateList("Bank.json",Bank)
    return

 
