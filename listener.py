directions = ["north","west","east","south"]
import time
from room import generate_room_info
def generate_doors(doors):
    door = ""
    for x in doors:
        door += x + " "
    return door

def status(play):
    print("You have",play[0],"hp and weild your",play[1][0],"along with these items:",generate_doors(play[1][1]))

def listener(dif, inp, current, player):
    inp = inp.lower()
    doors = current[2]
    if (inp in directions):
        if(inp in doors):
            print("you are moving",inp)
            return generate_room_info(dif, current, inp)
        else:
            print("can't go there")
            return current
    
    match inp:
        case "stop":
            print("come back soon")
            return []
        case "status":
            status(player)
            time.sleep(2)
            return current
        case "secret_code":
            if(player[0]<1):
                print("you've left this world")
                return []
            else:
                print("you left the old room")
            return generate_room_info(dif, current, inp)
        case _:
            print("not valid input")
            return current