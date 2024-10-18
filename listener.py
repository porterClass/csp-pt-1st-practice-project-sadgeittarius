directions = ["north","west","east","south"]
from room import generate_room_info
def listener(dif, inp, current, hp):
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
        case "explore":
            