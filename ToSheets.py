import Manage 
Fish = Manage.GetList("Fish.json")
String = ""

for Location in Fish:
    for Fishie in Fish[Location]:
        String += "true" + "|" + Location + "|" + Fishie[0] + "|" + str(Fishie[1]) + "|" + str(Fishie[2]) + "\n"

print(String)

