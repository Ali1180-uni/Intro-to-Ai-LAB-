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