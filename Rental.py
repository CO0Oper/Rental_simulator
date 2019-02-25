class Rental:
    def __init__(self, st_num, st_name, room, rent, distance):
        self.st_num = st_num
        self.st_name = st_name
        self.room = room
        self.rent = rent
        self.distance = distance

    def getNum(self):
        return self.st_num

    def getName(self):
        return self.st_name

    def getRoom(self):
        return self.room

    def getRent(self):
        return self.rent

    def getDistance(self):
        return self.distance





# array = genarateRnd(10)

# array = genarateNum(6, 10)

#print(200 + 50 * genarateNum(1, 7)[0])
