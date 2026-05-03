import discord
import os
import importlib
import sys
import random
import Manage
import time

intents = discord.Intents.default()
intents.message_content = True


ManualChannel = None
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
   

os.chdir("Commands")
Functions = os.listdir()
Fishers = Manage.GetList("Fishers.json")
Fishing = Manage.GetList("Fishing.json")
Fishies = Manage.GetList("Fish.json")

sys.path.append(os.getcwd())
import Inventory

Samesies = {
    "inv": "inventory",
    "fih": "fish"
}



@client.event

async def on_message(message):
    authorid = str(message.author.id)
    if message.author == client.user:
        return
    if message.content.startswith('%') or client.user in message.mentions:
        Content = message.content
        if client.user in message.mentions:
            Content = "%Random"
        Command = Content.split("%")[1]
        MainCommand = Command.split(" ")[0].lower()
        if message.content == "%": 
            MainCommand = "random"
        if MainCommand in Samesies:
            Command = Command.replace(MainCommand,Samesies[MainCommand])

        MainCommand = Command.split(" ")[0].lower()
        print(Command) 
        for FileName in Functions:
            CommandName = FileName.split(".py")[0]
            if CommandName.lower() == MainCommand:
                CommandModule = importlib.import_module(CommandName)
                Args = Command.split(" ")[1:]
                ToSend = CommandModule.Main(message.author,Args)
                await message.channel.send(ToSend)
        if Command.split(" ")[0].lower() == "fish":
            Args = Command.split(" ")[1:]
            
            if authorid in Fishers:
                await message.reply("Your already fishing")
            elif len(Args) != 1:
                await message.reply("Please Provide one Argument")
            else:
                FishingSpots = list(Fishies)
                if Args[0].lower() not in FishingSpots:
                    await message.reply("Please fish in one of these fishing spots: "+" | ".join(FishingSpots))
                else:
                    await message.reply("You have cast your rod, keep speaking and a fish may bite")
                    Fishers.append(authorid)
                    Fishing[authorid] = [Args[0].lower(),time.time() - 2,time.time()]
                    Manage.UpdateList("Fishers.json",Fishers)
                    Manage.UpdateList("Fishing.json",Fishing)

    if authorid in Fishers:
        rand =  random.randint(0,30)
        if (time.time() - Fishing[authorid][1]) > 2:
            Fishing[authorid][1] = time.time()
            if rand == 0 or (time.time() - Fishing[authorid][2]) > 1200 :
                CanFind = Fishies[Fishing[authorid][0]]
                Total = 0
                for Fish in CanFind:
                    Total += Fish[2]
                RandomWeight = random.randint(0,Total)
                Total = 0
                Found = False
                PickedFishNum = -1
                for Fish in CanFind:
                    if (Total == RandomWeight or RandomWeight < Total) and Found == False:
                        Found = True
                        PickedFishNum += 1 
                PickedFish = CanFind[PickedFishNum]
                Fishers.remove(authorid)
                del Fishing[authorid]
                Manage.UpdateList("Fishers.json",Fishers)
                Inventory.Add(message.author,PickedFish,"Fish")
                await message.reply(message.author.mention +" : Caught A **" + PickedFish[0] +"**!" )
            Manage.UpdateList("Fishing.json",Fishing)

                    

            
Info = Manage.GetList("Info.json")
client.run(Info["Token"] )
