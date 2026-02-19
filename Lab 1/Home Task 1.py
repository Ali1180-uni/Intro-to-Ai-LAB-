# Question 1

print("<-------Task 1: Celsius to Fahrenheit------->")
celsius = float(input("Enter a degree in Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")

# Question 2

print("\n<-------Task 2: Cylinder Volume------->")
length = int(input("Enter the length of a cylinder: "))
radius = int(input("Enter the radius of a cylinder: "))
area = radius * radius * 3.14
volume = area * length
print(f"The area is {area}")
print(f"The volume is {volume}")

# Question 3

print("\n<-------Task 3: Feet to Meters------->")
feet = float(input("Enter a value for feet: "))
meters = feet * 0.305
print(f"{feet} feet is {meters} meters")

# Question 4

print("\n<----Task 4: Pounds to Kilograms---->")
pounds = float(input("Enter a value in pounds: "))
kilograms = pounds * 0.454
print(f"{pounds} pounds is {kilograms} kilograms")

# Question 5

print("\n<----Task 5: Tip Calculator---->")
subtotal = int(input("Enter the subtotal: "))
rate = int(input("Enter the gratuity rate: "))
gratuity = subtotal * (rate / 100)
total = subtotal + gratuity
print(f"The gratuity is {gratuity} and the total is {total}")

# Question 6

print("\n<----Task 6: Payroll Application---->")
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
fed_tax_rate = float(input("Enter federal tax withholding rate: "))
state_tax_rate = float(input("Enter state tax withholding rate: "))
gross_pay = hours * pay_rate
fed_withholding = gross_pay * fed_tax_rate
state_withholding = gross_pay * state_tax_rate
total_deduction = fed_withholding + state_withholding
net_pay = gross_pay - total_deduction
print(f"\nEmployee Name: {name}")
print(f"Hours Worked: {hours}")
print(f"Pay Rate: ${pay_rate}")
print(f"Gross Pay: ${gross_pay}")
print("Deductions:")
print(f"  Federal Withholding ({fed_tax_rate * 100}%): ${fed_withholding}")
print(f"  State Withholding ({state_tax_rate * 100}%): ${state_withholding}")
print(f"  Total Deduction: ${total_deduction}")
print(f"Net Pay: ${net_pay}")

# Question 7

print("\n<----Task 7: Future Investment Value---->")
amount = float(input("Enter investment amount: "))
annual_rate = float(input("Enter annual interest rate: "))
years = int(input("Enter number of years: "))
monthly_rate = annual_rate / 1200
months = years * 12        
future_value = amount * ((1 + monthly_rate) * months)
print(f"Accumulated value is {future_value}")

# Question 8

print("\n<----Task 8: Miles to Kilometers---->")
miles = float(input("Enter a value in miles: "))
kilometers = miles / 0.6213
print(f"{miles} miles is {kilometers} kilometers")
