import turtle as t

# Question 1
# def rectangle(height, width):
#     t.pendown()
#     t.color("blue")
#     t.forward(width)
#     t.left(90)
#     t.forward(height)
#     t.left(90)
#     t.forward(width)
#     t.left(90)
#     t.forward(height)
#     t.penup()
#     t.hideturtle()
#     t.done()

# rectangle(100, 200)


# Question 2
# x1, y1 = input("Enter the coordinates of the point (x1, y1): ").split()
# x1, y1 = float(x1), float(y1)
# radius = float(input("Enter the radius of the circle: "))
# width = float(input("Enter the width of rectangle: "))
# height = float(input("Enter the height of rectangle: "))

# distance = (x1**2 + y1**2)**0.5


# t.penup()
# t.goto(0, -radius)
# t.pendown()
# t.color("green")
# t.circle(radius)

# t.penup()
# t.goto(-width/2, -height/2)
# t.pendown()
# t.color("blue")
# for _ in range(2):
#     t.forward(width)
#     t.left(90)
#     t.forward(height)
#     t.left(90)

# t.penup()
# t.goto(x1, y1)
# t.pendown()
# t.color("red")
# t.dot(10)

# t.penup()
# t.goto(x1, y1 - 20)
# if distance < radius:
#     t.write("Point is INSIDE the circle", align="center")
# else:
#     t.write("Point is OUTSIDE the circle", align="center")

# t.goto(x1, y1 - 40)
# if abs(x1) < width/2 and abs(y1) < height/2:
#     t.write("Point is INSIDE the rectangle", align="center")
# else:
#     t.write("Point is OUTSIDE the rectangle", align="center")

# t.hideturtle()
# t.done()


# Question 4
# class book:
#     def __init__(self, ISBN, title, price, Main_Area, Sub_Area, no_of_pages):
#         self.ISBN = ISBN
#         self.title = title
#         self.price = price
#         self.Main_Area = Main_Area
#         self.Sub_Area = Sub_Area
#         self.no_of_pages = no_of_pages

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Price: ${self.price}")
#         print(f"ISBN: {self.ISBN}")
#         print(f"Main Area: {self.Main_Area}")
#         print(f"Sub Area: {self.Sub_Area}")
#         print(f"Number of Pages: {self.no_of_pages}")

# book1 = book("1291", "Python", 29, "Programming", "Python", 350)
# book1.display_info()

# Question 5
# class Computer:
#     def __init__(self, brand_name, speed, memory_size):
#         self.brand_name = brand_name
#         self.speed = speed
#         self.memory_size = memory_size

#     def show(self):
#         print(f"Brand Name: {self.brand_name}")
#         print(f"Speed: {self.speed} GHz")
#         print(f"Memory Size: {self.memory_size} GB")

# computer1 = Computer("Dell", 3.5, 16)
# computer1.show()

# Question 6
# class Loan:
#     def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000, borrower=""):
#         self.__annualInterestRate = annualInterestRate
#         self.__numberOfYears = numberOfYears
#         self.__loanAmount = loanAmount
#         self.__borrower = borrower

#     def getAnnualInterestRate(self):
#         return self.__annualInterestRate

#     def getNumberOfYears(self):
#         return self.__numberOfYears

#     def getLoanAmount(self):
#         return self.__loanAmount

#     def getBorrower(self):
#         return self.__borrower

#     def setAnnualInterestRate(self, annualInterestRate):
#         self.__annualInterestRate = annualInterestRate

#     def setNumberOfYears(self, numberOfYears):
#         self.__numberOfYears = numberOfYears

#     def setLoanAmount(self, loanAmount):
#         self.__loanAmount = loanAmount

#     def setBorrower(self, borrower):
#         self.__borrower = borrower

#     def getMonthlyPayment(self):
#         monthlyInterestRate = self.__annualInterestRate / 1200
#         monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (self.__numberOfYears * 12))
#         return monthlyPayment

#     def getTotalPayment(self):
#         totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
#         return totalPayment

# loan1 = Loan(5, 15, 200000, "John Doe")
# print(f"Borrower: {loan1.getBorrower()}")
# print(f"Annual Interest Rate: {loan1.getAnnualInterestRate()}%")
# print(f"Number of Years: {loan1.getNumberOfYears()}")
# print(f"Loan Amount: {loan1.getLoanAmount()}")
# print(f"Monthly Payment: {loan1.getMonthlyPayment()}")
# print(f"Total Payment: {loan1.getTotalPayment()}")

# Question 6
# Implement BMI Class with following :
# Private Data Initializer: def __init__(self, name, age, weight, height):
#  Functions: getBMI(self):, getStatus: bmi = self.getBMI(), if bmi < 18.5: return "Underweight" etc., getName(self)
# getAge(self), getWeight(self), self.__weight, getHeight(self), 

class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        bmi = self.__weight / (self.__height ** 2)
        return bmi

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        else:
            return "Overweight"

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeight(self):
        return self.__height

bmi1 = BMI("Ali", 30, 70, 1.75)
print(f"Name: {bmi1.getName()}")
print(f"Age: {bmi1.getAge()}")
print(f"Weight: {bmi1.getWeight()} kg")
print(f"Height: {bmi1.getHeight()} m")
print(f"BMI: {bmi1.getBMI()}")
print(f"Status: {bmi1.getStatus()}")