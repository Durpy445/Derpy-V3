import Manage
import json
import random
import time
random.seed(time.time())
def Main(User,Args):
    JsonFile = Manage.Read("Responses.json")
    ResponseArray = json.loads(JsonFile)
    if len(Args) >= 2:
        if Args[0].lower() == "add" and User.id == 569611563745542174:
            Next = Args[1:]
            String = " ".join(Next)
            ResponseArray.append(String)
            Manage.UpdateList("Responses.json",ResponseArray)
            return "Added: " + String
    return random.choice(ResponseArray)
