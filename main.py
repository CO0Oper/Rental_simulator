from Rental import Rental
from Node import node, linked_list
import random

menu = [
    "h - display this help",
    "a - display all the rental properties on the current list",
    "f - switch to the favourite list",
    "u - switch to the undecided list",
    "l - 'swipe left' on the current rental property",
    "r - 'swipe right' on the current rental property",
    "n - skip to the next rental property",
    "sa - set the sorting to 'by address'",
    "sn - set the sorting to 'by number of rooms'",
    "sr - set the sorting to 'by rent'",
    "q - quit the program"
]

street_name = ["Mouse Ave", "Fox St.", "Coyote Crt.", "Cat st.", "Squirrel Crt.",
               "Maggot Ave", "Tapeworm St.", "Filariasis Crt.", "Whipworm St.", "Cestoda Ave."]

def interface():
    undecided = linked_list()
    favourite = linked_list()

    iniRental(undecided)




def display(num):
    for index in menu:
        print(index)



def iniRental(list):
    num = genarateNum(6, 1, 200)
    name = genarateRnd(6)
    room = genarateRndNum(6, 1, 3)
    rent = genarateNum(6, 1, 8)

    i = 0
    while i < 5:
        rental = Rental(num[i], street_name[name[i]], room[i], 200 + 50 * rent[i], 600 + (num[i] * 20 / 10))
        list.append(rental)
        i += 1

    for i in range(5):
        print(list.get(i).getNum(), list.get(i).getName(), list.get(i).getRoom(), list.get(i).getRent(),
              list.get(i).getDistance())



def genarateRnd(num):
    rndNum = []
    for index in range(num):
        rndNum.append(index + 1)

    for x in range(num):
        temp = rndNum[x]
        rnd = random.randint(0, num - 1)
        rndNum[x] = rndNum[rnd]
        rndNum[rnd] = temp

    return rndNum


def genarateNum(num, min, max):
    rndNum = []
    index = 0
    while index < num:
        rnd = random.randint(min, max + 1)
        if rnd not in rndNum:
            rndNum.append(rnd)
            index += 1

    return rndNum

def genarateRndNum(num, min, max):
    rndNum = []
    index = 0
    while index < num:
        rnd = random.randint(min, max+1)
        rndNum.append(rnd)
        index += 1
    return rndNum




