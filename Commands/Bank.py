import Manage
def Main(User,Args):
    Bank = Manage.GetList("Bank.json")
    UserId = User.id
    if UserId not in Bank:
        return "Broke Bih"
    MoneyCoins = Bank[UserId]
    return User.mention + " has: **" + MoneyCoins + "** Money Coins"

def Add(User,Amount):
    Bank = Manage.GetList("Bank.json")
    UserId = User.id
    if UserId not in Bank:
        Bank[UserId] = str(Amount)
        return
    Bank[UserId] = str(int(Bank[UserId]+int(Amount)))
    Manage.UpdateList("Bank.json",Bank)
    return

 
