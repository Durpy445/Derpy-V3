import os
import json

print("CWD", os.getcwd())
storageLocation = os.getcwd() + "/Commands/Storage/"

def Read(FileName):
    File = open(storageLocation + FileName)
    return File.read()

def GetFile(FileName):
    File = open(storageLocation +FileName)
    return File

def Write(FileName,ToWrite):
    File = open(storageLocation +FileName,"w")
    File.write(ToWrite)

def Append(FileName,ToAppend):
    File = open(storageLocation +FileName,"a")
    File.write(ToAppend)


def GetList(FileName):
    JsonFile = Read(FileName)
    return json.loads(JsonFile)

def UpdateList(FileName,NewList):
    JsonString = json.dumps(NewList)
    Write(FileName,JsonString)
    pass
