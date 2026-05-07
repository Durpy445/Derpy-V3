import Manage
import time
import os
import discord

BlockFolder = Manage.GetList("Info.json")["MCTextureFolder"]

Textures = os.listdir("/home/n3bxi/Storage/Jar/assets/minecraft/textures/block/")

def Main(User,Args):
    print ( len(Args))
    print(Args)
    TurtleIO = Manage.GetList("TurtleIO.json")
    Args[0] = Args[0].lower()
    if Args[0] == "left":
        Args[0] = "back"
    if Args[0] == "right":
        Args[0]= "forward"
    TurtleIO["Input"] = Args[0]
    Manage.UpdateList("TurtleIO.json",TurtleIO)
    StartTime = time.time()
    while Manage.GetList("TurtleIO.json")["Output"] == "":
        time.sleep(0.1)
        if time.time() - StartTime > 5:
            return "Derpy Is Either Broken, Or the server is offline"
    Output = Manage.GetList("TurtleIO.json")["Output"] 
    TurtleIO = {"Input":"","Output":""}
    Manage.UpdateList("TurtleIO.json",TurtleIO)
    Emojis = Manage.GetList("Emojis.json")
    
    if Output.split("@@@")[0] == "Sight":
        Splitted = Output.split("@@@")[1].split("|")
        ReturnString = ""
        Numb = 0
        Line = ""
        Lines = []
        for Block in Splitted[::-1]:
            if Block + ".png" in Textures:
                emoji = discord.utils.get(Args[1], name=Block)
                ReturnString += str(emoji)
                print(ReturnString)
            else:
                Total = 0
                for Letter in Block:
                    Total += ord(Letter)
                Emoji = Emojis[Total % len(Emojis)]
                ReturnString += Emoji
            Numb += 1
            if Numb % 5 == 0:
                Lines.append(ReturnString)
                ReturnString = ""
        Lines = Lines[::-1]
        ReturnString = ""
        for Line in Lines:
            ReturnString += Line + "\n"

        print(ReturnString)
        return ReturnString
    elif Output.split("@@@")[0] == "Inv":
        ReturnString = ""
        Splitted = Output.split("@@@")[1].split("\n")

        for Slot in Splitted:
            print(Slot)
            Name = Slot.split(":")[0]
            Count = Slot.split(":")[1]
            if Name + ".png" in Textures:
                emoji = discord.utils.get(Args[1], name=Name)
                ReturnString += str(emoji)
            else:
                ReturnString += Name
            ReturnString += ":"+ str(Count)
            ReturnString += "\n"

        return ReturnString
    return("Odd")

