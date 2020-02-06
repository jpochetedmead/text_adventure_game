from escape_game import *

correctPath = random.randint(1, 5)

class Rooms(object):
    def __init__(self, theroom):
        self.theroom = theroom

    def whereat(self):
        for line in self.theroom:
            print(line)

living_room = Rooms([
    "You are in the living room"
])

kitchen = Rooms([
    "You are in the kitchen"
])

bedroom = Rooms([
    "You are in the bedroom"
])

bathroom = Rooms([
    "You are in the bathroom"
])

basement = Rooms([
    "You are in the basement"
])


def room01(self):
    cls()

    #print("\n \n --> You are in Room 01 now")

    living_room.whereat()

    if user_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")


def room02():
    cls()

    #print("\n \n --> You are in Room 02 now")

    kitchen.whereat()

    if user_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")

def room03():
    cls()

    #print("\n \n --> You are in Room 03 now")

    bedroom.whereat()

    if user_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")

def room04():
    cls()

    #print("\n \n --> You are in Room 04 now")

    bathroom.whereat()

    if user_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")

def room05():
    cls()

    #print("\n \n --> You are in Room 05 now")

    basement.whereat()

    if user_choice == correctPath:
        print("Good Job, you are still alive!")
    else:
        print("Chucky just killed you in the most bloody way o.O")
