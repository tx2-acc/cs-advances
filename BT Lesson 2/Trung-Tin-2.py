from datetime import datetime 

#BT1: 
class Rectangle: 
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self): 
        return f"Rectangle object with height = {self.height} and width = {self.width}."

newRect = Rectangle(2, 1)
print(newRect)

#BT2: 
class MathList:
    def __init__(self, uList):
        self.uList = uList

    def __add__(self, uInt):
        return [x + uInt for x in self.uList]
    
    def __sub__(self, uInt):
        return [x - uInt for x in self.uList]

    def __str__(self):
        return f"{self.uList}"

testList = [1, 2, 3, 4, 5]
newMList = MathList(testList)
print(newMList)

newMList += 2
print(newMList)

#BT3: 
class Square:
    def __init__(self, edge):
        self.edge = edge

    def cal_area(self):
        return self.edge**2

class Cube(Square):
    def cal_area(self):
        return (6*self.edge**2)
    
    def cal_volume(self):
        return self.edge**3

newSquare = Square(2)
print('Square area:', newSquare.cal_area())

newCube = Cube(2)
print('Cube area:', newCube.cal_area())
print('Cube volume:', newCube.cal_volume())

#BT4: 
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def welcome(self):
        print(f"Welcome, {self.username}.")
    
    def checkPassword(self, toCheck): 
        return toCheck == self.password
    
class SubscribedUser(User):
    def __init__(self, username, password, expiredDate):
        self.username = username
        self.password = password
        self.expiredDate = expiredDate

    def is_expired(self): 
        getCurrentTime = datetime.now()
        timeLeft = (self.expiredDate - getCurrentTime).days
        return timeLeft <= 0

    

newUser = User("user", 12345)
newUser.welcome()
print(newUser.checkPassword("testPassword2"))

newSubUser = SubscribedUser("sub_user", 12345, datetime(2024, 1, 1))
print(newSubUser.is_expired())