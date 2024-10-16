from random import *
import math
def generate_room_info(dif):
    enemy = enemyChances[abs(round(normalvariate(0,dif)))]
    item = itemChances[abs(round(normalvariate(0,2)))]
    doors = [doorChances[round(randint(1,4))],doorChances[round(randint(1,4))]]
    return [enemy,item,doors]

enemyChances = {
  0: "puppy",
  1: "",
  2: "goblin",
  3: "slime",
  4: "fairy"
}

itemChances = {
  0: "nothing",
  1: "knife",
  2: "sword",
  3: "bread",
  4: "key"
}

doorChances = {
  1: "west",
  2: "north",
  3: "east",
  4: "south"
}
