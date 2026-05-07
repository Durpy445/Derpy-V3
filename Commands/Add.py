import Manage
def Main(User,Args):
    if User.id == 569611563745542174:
        if Args[0].lower() == "fish":
            Location = Args[1].lower()
            Name = Args[2]
            Name = Name.replace("\\"," ")
            Value = Args[3]
            Weight = Args[4]
            
            New = False
            if len(Args) == 6:
                if Args[5].lower() == "true":
                    New = True

            Fishies = Manage.GetList("Fish.json")
            if Location in Fishies:
                Fishies[Location].append([Name,int(Value),int(Weight)])
                Manage.UpdateList("Fish.json", Fishies)
                return "Added: " +Name + " To " + Location
            elif New == True:
                Fishes[Location] = [[Name,int(Value),int(Weight)]]
                Manage.UpdateList("Fish.json", Fishies)
                return "Added: " + Name + " To " + Location
        if Args[0].lower() == "explore":
            Location = Args[1].lower()
            Name = Args[2]
            Name = Name.replace("\\"," ")
            Value = int(Args[3])
            Weight = Args[4]
            Type = Args[5]
            
            New = False
            if len(Args) == 7:
                if Args[6].lower() == "true":
                    New = True
            
            Exploring = Manage.GetList("Exploring.json")
            if Location in Exploring:
                Exploring[Location].append([[Name,Value],Type,Weight])
                Manage.UpdateList("Exploring.json",Exploring)
                return "Added: " +Name + " To " + Location
            if New == True:
                Exploring[Location].append([[Name,Value],Type,int(Weight)])
                Manage.UpdateList("Exploring.json",Exploring)
                return "Added: " +Name + " To " + Location
        if Args[0].lower() == "emoji":
            NewArgs = Args[1:]
            Emojis = Manage.GetList("Emojis.json")
            for NewEmoji in NewArgs:
                if NewEmoji not in Emojis:
                    Emojis.append(NewEmoji)
            Manage.UpdateList("Emojis.json",Emojis)
            return Emojis
                



        return "False"
            


