Fish = {}
import Manage
while True:
    Input = input("")
    if Input == "|||":
        break
    Split = Input.split("|")
    if Split[0] not in Fish:
        Fish[Split[0]] = []
    Fish[Split[0]].append([Split[1],int(Split[2]),int(Split[3])])

Manage.UpdateList("Fish.json",Fish)

