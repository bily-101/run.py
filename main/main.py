
import random,sys,time,os,re
import os.path
from os import path
def printt(thingggg,dela=.04):
  for i in thingggg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(dela)
  print("")
def readName():
    f=open("name.txt", "r")
    if f.mode == 'r':
        name =f.read()
        return(f"{name}")
def readList():
    f=open("thingsICanDO.txt")
    if f.mode == 'r':
        info =f.read()
    return info
def questionsAsk(questionnn):
    if (questionnn == "What can you do?" or questionnn == "WHAT CAN YOU DO??" or questionnn == "WHAT CAN YOU DO" or questionnn == "what can you do" or questionnn == "what can you do?"):
        readList()
    

if(path.exists("name.txt")): 
    f=open("name.txt", "r")
    if f.mode == 'r':
        name =f.read()
        printt(f"Hi {name}")
else:
    printt("What is your name?")
    name=input(": ")
    f= open("name.txt","w+")
    f.write(f"{name}")
    printt(f"Hi {name}")

printt("How are you feeling?")
feeling=input(": ")

printt("My name is bily-101 would you like to chat with me?")
option=input(": ")

if (option == "yes" or option=="YES" or option=="ye"):
    printt("Alright so wassup")
    questionOne = input(": ")

else:
    printt("Ok... you want a list of things I can do?")
    option = input(": ")
    print(questionsAsk(option))
    input(": ")
