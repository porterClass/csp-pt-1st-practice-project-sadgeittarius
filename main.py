from random import *
from room import *
from listener import *
import time

inv = ["hands",["","bread"]]#[weapon, item list]
alive = True
dif = 2
hp = 3
player = [hp,inv]
currentRoom = generate_room_info(dif, ["","",[]],"")

def introduction():
    print("Welcome to the Dungeon Escape!")
    print("Your goal is to explore the dungeon, collect items, and find a teleporter to the Final Boss.")
    print("Good luck!")

def explore_room(current,play):
    print("you have met a ", current[0])
    time.sleep(1)
    enemy = current[0]
    global hp
    old = hp
    hp+=enemyEncounter(enemy)
    hp+=itemBuff(play[1][1])
    if(hp>old):
        hp=old
    global player 
    print("after your encounter you have: "+str(hp)+" hp")
    
    print("you have found a",current[1])
    if(current[1] == "gate"):
        boss_encounter(play)
    it=True
    while(it and current[1] != "nothing" and current[1] != "gate"):
        inp = input("do you want the item. 'y' or 'n'")
        match inp:
            case "y":
                it=False
                if(current[1]=="sword" or current[1] == "knife"):
                    play[1][0] = current[1]
                    player = [hp,play[1]]
                else:
                    play[1][1].append(current[1])
                    player=[hp,play[1]]
            case "n":
                it=False
            case _:
                print("invalid input")
    return "secret_code"

def boss_encounter(play):
    print("you are entering the gate")
    time.sleep(2)
    print("the battle begins")
    time.sleep(0.5)
    print("you raise your",play[1][0],"and prepared for the battle of a lifetime, knowing that defeat was not an option.")
    time.sleep(1)
    print("The battle commences")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    if((play[0]>=2 and play[1][1] == "sword") or (play[0]>=3 and play[1][1] == "knife") or (play[0]>=4 and play[1][1] == "hands")):
        print("you barely won, good game")
    else:
        print("you lost horribly")
    global alive
    alive = False
    return "dead"

introduction()

while(alive):
    print("--------------------------------------------------------------------------------------------------------------")
    print("type 'stop' to end the game")
    print("type an item's name to use it")
    print("you have entered a room with doors", generate_doors(currentRoom[2])+"\ntype 'explore', a direction to move, or 'status'")
    print(currentRoom)#remove this later
    inp = input("")
    oldRoom = currentRoom
    if(inp == "explore"):
        x = explore_room(currentRoom, player)
        if x=="secret_code":
            status(player)
            currentRoom = listener(dif, "secret_code", currentRoom, player)
        time.sleep(3)
    elif(inp == "bread"):
        if(inp in player[1][1]):
            print("you eat your bread")
            hp+=1
            player = [hp,player[1]]
            player[1][1].remove("bread")
            time.sleep(1)
            print("you feel rejuvenated")
            time.sleep(1)
        else:
            print("you have no", inp)
            time.sleep(1)
    else:
        currentRoom = listener(dif, inp, currentRoom,player)
    if(len(currentRoom)<3 or hp<=0):
        print("good game")
        alive=False
    elif(currentRoom!=oldRoom):
        dif+=1