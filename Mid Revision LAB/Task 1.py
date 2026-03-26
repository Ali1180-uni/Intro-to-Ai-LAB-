import turtle as t
# Question 1
# x = input("Enter a Degree in Celsius: ")
# fahrenheit = (9/5) * float(x) + 32
# print(f"The {x} Celsius is {fahrenheit} Fahrenheit.")

# Question 2
# r,l = input("Enter the radius and length of a cylinder: ").split()
# area = float(r)**2 * 3.14
# volume = area * float(l)
# print(f"The area is {area}")
# print(f"The volume is {volume}")

# Question 3
# name = input("Enter your name: ")
# hours = input("Enter hours you work: ")
# pay = input("Enter your hourly pay rate: ")
# f_tax = input("Enter your federal tax rate: ")
# s_tax = input("Enter your state tax rate: ")
# gross_pay = float(hours) * float(pay)
# f_tax_amount = gross_pay * float(f_tax)
# s_tax_amount = gross_pay * float(s_tax)
# net_pay = gross_pay - f_tax_amount - s_tax_amount
# print(f"Employee Name: {name}")
# print(f"Gross Pay: {gross_pay}")
# print(f"Federal Withholding (20%): {f_tax_amount}")
# print(f"State Tax (9%): {s_tax_amount}")
# print(f"Net Pay: {net_pay}")

# Question 4
# amount = float(input("Enter investment amount: "))
# annual_rate = float(input("Enter annual interest rate: "))
# years = float(input("Enter number of years: "))
# future_value = amount * (1 + annual_rate / 1200) ** (years * 12)
# print(f"Accumulated value is {future_value}")

# Question 5
# x = input("Enter point x: ")
# y = input("Enter point y: ")
# width = 10
# height = 5
# r = 10
# circle = float(x)**2 + float(y)**2 < r**2
# print(f"Point ({x}, {y}) is {'inside the circle' if circle else 'outside the circle'}")
# rectangle = abs(float(x)) <= width/2 and abs(float(y)) <= height/2
# print(f"Point ({x}, {y}) is {'inside the rectangle' if rectangle else 'outside the rectangle'}")

# Question 6
# class Book:
#     def __init__(self, ISBN, Title, Price, Main_Area, Sub_Area, Pages):
#         self.ISBN = ISBN
#         self.Title = Title
#         self.Price = Price
#         self.Main_Area = Main_Area
#         self.Sub_Area = Sub_Area
#         self.Pages = Pages

#     def display(self):
#         print(f"ISBN: {self.ISBN}")
#         print(f"Title: {self.Title}")
#         print(f"Price: ${self.Price:.2f}")
#         print(f"Main Area: {self.Main_Area}")
#         print(f"Sub Area: {self.Sub_Area}")
#         print(f"Pages: {self.Pages}")

# print("<-------------Book 1------------->")
# book1 = Book("978-3-16-148410-0", "Python Programming", 29.99, "Computer Science", "Programming", 350)
# book1.display()
# print("<-------------Book 2------------->")
# book2 = Book("978-0-13-419044-0", "Data Structures and Algorithms", 39.99, "Computer Science", "Algorithms", 500)
# book2.display()

# Question 7
class Loan:
    def __init__(self):
        self.__annualInterestRate = 2.5
        self.__numberOfYears = 1
        self.__loanAmount = 1000
        self.__borrower = ''
    
    def setAnnualInterestRate(self, rate):
        self.__annualInterestRate = rate

    def setNumberOfYears(self, years):
        self.__numberOfYears = years

    def setLoanAmount(self, amount):
        self.__loanAmount = amount

    def setBorrower(self, borrower):
        self.__borrower = borrower

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    def getMonthlyPayment(self):
        monthly_rate = self.__annualInterestRate / 1200
        return monthly_rate

    def getTotalPayment(self):
        return self.getMonthlyPayment() * self.__numberOfYears * 12

loan = Loan()