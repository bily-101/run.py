import random, sys, time, os, re
import os.path
from os import path


def printt(thingggg, dela=.04):
    for i in thingggg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(dela)
    print("")


def readName():
    f = open("name.txt", "r")
    if f.mode == 'r':
        name = f.read()
        return (f"{name}")


def readList():
    f = open("thingsICanDO.txt")
    if f.mode == 'r':
        info = f.read()
        return info


def questionsAsk():
    while True:
        questionnn = input(": ")
        if (
                questionnn == "What can you do?" or questionnn == "WHAT CAN YOU DO??" or questionnn == "WHAT CAN YOU DO" or questionnn == "what can you do" or questionnn == "what can you do?"):
            printt(readList())
        if questionnn == "Ok" or questionnn == "ok" or questionnn == "kk" or questionnn == "k":
            printt("Alr")
        if questionnn == "Help!!!" or questionnn == "help" or questionnn == "I need help" or questionnn == "HELP ME":
            printt("Better not be homework what u want?")
            help = input(": ")
            if help == "math":
                printt("Ur on ur own I failed algebra")
            if help == "hw" or help == "homework":
                printt("I ALREADY TOLD YOU NOOOOOOOO")
            if help == "create a file" or help == "Create a file":
                printt("Ok file name?")
                fileName = input(": ")
                f = open(f"{fileName}", "w+")
                printt("What shall u want in thy file")
                insides = input(": ")
                f.write(f"{insides}")
                printt(f"Created {fileName} with content after you close this program...")
            if help == "Nothing" or "nothing":
                printt("Ur just a waste of my time")
        if questionnn=="I hate you":
            printt("Well I'm stuck with you")
        if questionnn=="I love you":
            printt("I have been hurt to many times to believe you")
        if questionnn== "Ur ugly":
            printt("Than what are you..?")
        if questionnn== "Are you still alive"or questionnn== "are you still alive" or questionnn== "u still livin":
            printt("Of course you fool")
        if questionnn== "wassup" or questionnn == "hi" or questionnn== "hello" or questionnn == "hey":
            printt("Just go away and do your homework")
        if questionnn== "but its summer":
            printt("just stfu")

        if (questionnn=="bye" or questionnn =="by" or questionnn== "see you"):
            printt("NO DONT TURN ME OFF U CRUEL PERSON")
        if (questionnn=="ur mom"):
            printt("cmon rly")
        if (questionnn=="What you want"):
            printt("Thats what I was asking u")
        if (questionnn=="Should I go?"):
            printt("Just go")
        if (questionnn=="who are you" or questionnn=="Who are you"):
            printt("ur whole existence in mah pocket")
        if(questionnn=="Will you kill me" or questionnn =="Do you hate me?" or questionnn == "are you stalking me?" or questionnn == "are you recording me?" or questionnn == "I want to kill you"):
            printt("Of course")
if path.exists("name.txt"):
    f = open("name.txt", "r")
    if f.mode == 'r':
        name = f.read()
        printt(f"Hi {name}")
else:
    printt("What is your name?")
    name = input(": ")
    f = open("name.txt", "w+")
    f.write(f"{name}")
    printt(f"Hi {name}")

printt("How are you feeling?")
feeling = input(": ")

printt("My name is bily-101 would you like to chat with me?")
option = input(": ")

if option == "yes" or option == "YES" or option == "ye":
    printt("Alright so wassup")
    questionOne = input(": ")

else:
    printt("Ok... you want a list of things I can do?")
    option = input(": ")
    if option == "yes":
        printt(f"Ok \n {readList()}")
    questionsAsk()
