import discord
import os
import importlib
import sys
import random
import Manage
import time

random.seed(time.time())
intents = discord.Intents.default()
intents.message_content = True


ManualChannel = None
client = discord.Client(intents=intents)

ClientEmojis = []
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


   

os.chdir("Commands")
Functions = os.listdir()
fishers = Manage.GetList("Fishers.json")
fishing = Manage.GetList("Fishing.json")
fishies = Manage.GetList("Fish.json")

sys.path.append(os.getcwd())
import Inventory

Samesies = {
    "inv": "inventory",
    "fih": "fish",
    "turtle": "minecraft",
    "up": "minecraft up",
    "down": "minecraft down",
    "left": "minecraft left",
    "right": "minecraft right"
}





@client.event
async def on_message(message):
    authorid = str(message.author.id)
    if message.author == client.user:
        return
    if message.content.startswith('%') or client.user in message.mentions:
        Content = message.content
        if client.user in message.mentions:
            Content = "%random"
        if message.content == "%":
            Content =  "%random"
        Command = Content.split("%")[1]
        MainCommand = Command.split(" ")[0].lower()
        
        if MainCommand in Samesies:
            Command = Command.replace(MainCommand,Samesies[MainCommand])

        MainCommand = Command.split(" ")[0].lower()
        print(Command)
        UserToSend = message.author
            
        for FileName in Functions:
            CommandName = FileName.split(".py")[0]
            if CommandName.lower() == MainCommand:
                CommandModule = importlib.import_module(CommandName)
                Args = Command.split(" ")[1:]

                global ClientEmojis
                if MainCommand == "minecraft":
                    if len(Args) > 1:
                        Args[1] =  await client.fetch_application_emojis()
                    else:
                        Args.append( await client.fetch_application_emojis())
                ToSend = CommandModule.Main(UserToSend,Args)
                await message.channel.send(ToSend)
        if Command.split(" ")[0].lower() == "fish":
            Args = Command.split(" ")[1:]
           

            
            if authorid in fishers:
                await message.reply("Your already fishing")
            elif len(Args) != 1:
                await message.reply("Please Provide one Argument")
            else:
                fishingSpots = list(fishies)
                if Args[0].lower() not in fishingSpots:
                    await message.reply("Please fish in one of these fishing spots: "+" | ".join(fishingSpots))
                else:
                    await message.reply("You have cast your rod, keep speaking and a fish may bite")
                    fishers.append(authorid)
                    fishing[authorid] = [Args[0].lower(),time.time() - 2,time.time()]
                    Manage.UpdateList("fishers.json",fishers)
                    Manage.UpdateList("fishing.json",fishing)

    if authorid in fishers:
        rand =  random.randint(0,30)
        if (time.time() - fishing[authorid][1]) > 2:
            fishing[authorid][1] = time.time()
            if rand == 0 or (time.time() - fishing[authorid][2]) > 1200 :
                CanFind = fishies[fishing[authorid][0]]
                Total = 0
                for fish in CanFind:
                    Total += fish[2]
                RandomWeight = random.randint(0,Total)
                Total = 0
                Found = False
                PickedfishNum = -1
                for fish in CanFind:
                    if (Total == RandomWeight or RandomWeight < Total) and Found == False:
                        Found = True
                        PickedfishNum += 1 
                Pickedfish = CanFind[PickedfishNum]
                fishers.remove(authorid)
                del fishing[authorid]
                Manage.UpdateList("fishers.json",fishers)
                Inventory.Add(message.author,Pickedfish,"fish")
                await message.reply(message.author.mention +" : Caught A **" + Pickedfish[0] +"**!" )
            Manage.UpdateList("fishing.json",fishing)

                    

            
Info = Manage.GetList("Info.json")
client.run(Info["Token1"] )
