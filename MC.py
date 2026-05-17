import asyncio
from websockets.asyncio.server import serve
import json
import time
import Manage


async def echo(websocket):
    async for message in websocket:
        if message == "Ready":
            while  Manage.GetList("TurtleIO.json")["Input"] == "":
                time.sleep(0.1)
            await websocket.send(Manage.GetList("TurtleIO.json")["Input"] )
        else:
            print(message)

            if "Sight@@@" in message:
                Talbe = json.loads(message.split("@@@")[1])
                Total = 0
                String = ""
                for Block in Talbe[::-1]:
                    String += Block["name"].split(":")[1] 
                    Total += 1
                    if Total != 25:
                        String += "|"

                Manage.UpdateList("TurtleIO.json",{"Input":"","Output":"Sight@@@" +String})
            elif "Inv@@@" in message:
                
                List = json.loads(message.split("@@@")[1])
                String = ""
                i = 0
                for Slot in List:
                    print(type(Slot))
                    print("A")
                    if i != 16:
                        i +=1
                        print(Slot)
                        if Slot == None:
                            Slot = {}
                            Slot["name"] = "minceraft:air"
                            Slot["count"] = 0
                        if List[16] == i:
                            String += Slot["name"].split(":")[1] + ":" + str(Slot["count"])+ " (Selected)" +"\n"
                        else:
                            String += Slot["name"].split(":")[1] + ":" + str(Slot["count"]) +"\n"

                String = String[:-1]
 
                Manage.UpdateList("TurtleIO.json",{"Input":"","Output": "Inv@@@" + String})
                
                

   
async def main():
    async with serve(echo, "192.168.0.205", 8765) as server:
        await server.serve_forever()



asyncio.run(main())

