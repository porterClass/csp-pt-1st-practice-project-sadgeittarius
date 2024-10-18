
from random import *
from room import *
from listener import *

def introduction():
    print("Welcome to the Dungeon Escape!")
    print("Your goal is to explore the dungeon, collect items, and find a teleporter to the Final Boss.")
    print("Good luck!")

def generate_doors(doors):
    door = ""
    for x in doors:
        door += x + " "
    return door
inv = ["hands",[]]#[weapon, item list]
alive = True
dif = 2
hp = 3
currentRoom = generate_room_info(dif, ["","",[]],"")

introduction()

while(alive):
    print("type 'help' if you need it, or 'stop' to end the game")
    print("you have entered a room with doors", generate_doors(currentRoom[2])+"\ntype 'explore', a direction to move, or 'status'")
    print(currentRoom)
    inp = input("")
    oldRoom = currentRoom
    currentRoom = listener(dif, inp, currentRoom, hp)
    if(len(currentRoom)<3 or hp<=0):
        alive=False
    elif(currentRoom!=oldRoom):
        dif+=1