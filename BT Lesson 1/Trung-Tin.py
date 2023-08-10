import datetime 

#BT1:
print("\nBT1:")
class Employee: 

    def __init__(self, name, position):
        self.name = name
        self.position = position
        

    def say_hi(self):
        print(f"Hi, my name is {self.name}.")

    def tell_position(self):
        print(f"I am a {self.position}.")

john = Employee("John", "Software Engineer")
john.say_hi()
john.tell_position()

#BT2:
print("\nBT2:")
uInput = input("Shape (rectangle / circle): ")
if uInput == "rectangle":
    hInput = int(input("Height: "))
    wInput = int(input("Width: "))
    rPerimeter = 2*(hInput + wInput)
    rArea = hInput*wInput
    print(f"Perimeter: {rPerimeter}.\nArea: {rArea}.")

elif uInput == "circle": 
    rInput = int(input("Radius: "))
    cPerimeter = 2*3.14*rInput 
    cArea = 3.14*(rInput**2)
    print(f"Perimeter: {cPerimeter}.\nArea: {cArea}.")
else:
    print("Invalid.")

#BT3: 
print("\nBT3:")
class CustomDate:
    time = datetime.datetime.now()

    def get_date(self): 
        print(f"{self.time.strftime('%d/%m/%Y')}")

    def get_time(self):
        print(f"{self.time.strftime('%H:%M:%S')}")

now = CustomDate()
now.get_date()
now.get_time()

#BT4: 
print("\nBT4:")
class DateHandler:
    def format_date(self, year, month, day):
        date = datetime.datetime(year, month, day)
        print(f"{date.strftime('%d/%m/%Y')}")

    def get_days_between(self):
        startInput = input("Start date (DD/MM/YY): ").split("/")
        endInput = input("End date (DD/MM/YY): ").split("/")
        mapped = [int(x) for x in startInput], [int(y) for y in endInput]
        start_date = datetime.datetime(mapped[0][2], mapped[0][1], mapped[0][0])
        end_date = datetime.datetime(mapped[1][2], mapped[1][1], mapped[1][0])
        print(f"Days between: {(end_date - start_date).days}.")

newDate = DateHandler()
newDate.format_date(2022, 1, 1)
newDate.get_days_between()