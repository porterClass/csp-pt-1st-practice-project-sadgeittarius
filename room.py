import random

enemyChances = {
  0: "puppy",
  1: "slime",
  2: "goblin",
  3: "cat",
  4: "fairy"
}

itemChances = {
  0: "nothing",
  1: "knife",
  2: "sword",
  3: "bread",
}

door = ["north", "south", "east", "west"]

def generate_part(x, dict):
    if(x not in dict.keys()):
        return dict[0]
    return dict[x]

def generate_doors(inp):
    lis=[]
    while(len(lis) == 0):
      lis = random.choices(door, weights = [1,1,1,1], k = 2)
      lis = list(dict.fromkeys(lis))
      if inp in lis:
          lis.remove(inp)
    return lis

def generate_room_info(dif,current, inp):
    enemy = generate_part(abs(round(random.normalvariate(0,dif))),enemyChances)
    item = generate_part(abs(round(random.normalvariate(0,2))), itemChances)
    if(dif>7):
        item = "gate"
    doors = generate_doors(inp)
    return [enemy,item,doors]

def enemyEncounter(enemy):
    match enemy:
        case "goblin":
            return -2
        case "slime":
            return -1
        case "fairy":
            return 3000
        case _:
            return 0
        
def itemBuff(item):
    match item:
        case "hands":
            return 0
        case "knife":
            return .5
        case "sword":
            return 1.5
        case _:
            return -1