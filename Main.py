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
fishers = Manage.GetList("fishers.json")
fishing = Manage.GetList("fishing.json")
fishies = Manage.GetList("Fish.json")

sys.path.append(os.getcwd())
import Inventory

Samesies = {
    "inv": "inventory",
    "fih": "fish",
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
                    print(Args)
                    Args.append( await client.fetch_application_emojis())
                ToSend = CommandModule.Main(UserToSend,Args)
                if ToSend == "plot.png":
                    file = discord.File("./Storage/plot.png",filename = "plot.png")
                    await message.channel.send(file=file)
                else:
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
        rand = 0
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

    if "barracuda" in message.content.lower():
        cuda = ["https://cdn.discordapp.com/attachments/1465411765062991914/1505537600830836878/caption.gif?ex=6a0afca7&is=6a09ab27&hm=f43ab0e835c6392776cd5a41347c022b93d0554350bf698c3999108e3052b2d6&",
         "https://cdn.discordapp.com/attachments/1465411765062991914/1505537600830836878/caption.gif?ex=6a0afca7&is=6a09ab27&hm=f43ab0e835c6392776cd5a41347c022b93d0554350bf698c3999108e3052b2d6&",
         "https://cdn.discordapp.com/attachments/1465411765062991914/1505538051940679750/captionTwo.gif?ex=6a0afd13&is=6a09ab93&hm=56f9f342aeff1b8966b6e3e8ccdba7e3e1c5540ae64da04f094538c86f3cd70b&",
         "https://cdn.discordapp.com/attachments/1465411765062991914/1505538462378361002/caption.png?ex=6a0afd74&is=6a09abf4&hm=9fcb828a289699cc604c2a5f32a150f3e348dcf2eed97f507f7adee5fb554342&",
         "https://cdn.discordapp.com/attachments/1465411765062991914/1505539367580598293/captionTwo.png?ex=6a0afe4c&is=6a09accc&hm=0cfa27dc71a8ad95d5845e709701a4853739e774d47b3148869986b4218c15fa&",
         "https://cdn.discordapp.com/attachments/1465411765062991914/1505539683894169650/caption.webp?ex=6a0afe98&is=6a09ad18&hm=823260879e8246fbc327fba9adc2471d3c12113de54e86b85eeefb32730819ff&",
         "https://cdn.discordapp.com/attachments/1184137342034907176/1505540504912138381/caption.d812ea77.gif?ex=6a0aff5b&is=6a09addb&hm=adbcd6000de54d3ca34ae4e94d022ea440057fed8043dd7bd15b280b651b76bc&",
         "https://cdn.discordapp.com/attachments/1184137342034907176/1505540996405002354/caption.9b082fa6.gif?ex=6a0affd1&is=6a09ae51&hm=818c72aa342651243338a2aa9cafc5dd679e6ddcb7be55557d97185c16492565&",
         "https://cdn.discordapp.com/attachments/1184137342034907176/1505541527684911204/caption.8869859f.gif?ex=6a0b004f&is=6a09aecf&hm=dce18bb06925f7c49704f54e290933b6f45f718a17abdc72dbb8792c6bdf93c8&",
         "https://cdn.discordapp.com/attachments/1184137342034907176/1505541816248963153/caption.db6dda0a.png?ex=6a0b0094&is=6a09af14&hm=d482150d60f533f2ae5ec4758faeb2ec87fbe59562b8471ff5a3978667f68d30&",
         "https://cdn.discordapp.com/attachments/1184137342034907176/1505542078875303956/caption.51b6c122.gif?ex=6a0b00d3&is=6a09af53&hm=bd07ffab8ad2d576ce5d62e41816278018eb7036f278d8d095b7e84bdfd906a6&",]
        
        await message.reply(random.choice(cuda))

                    

            
Info = Manage.GetList("Info.json")
client.run(Info["Token1"] )
