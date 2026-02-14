# Slide 18

age = 45
salary = 1456.8
name = "John"
x=y=z=45
i,j,k = "orange","banana","cherry"

print(age)
print("Salary = ", salary)
print("Name = ", name)

# Slide 20

name = input("Enter Your Name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter Your Salary: "))

print(type(name))
print(type(age))
print(type(salary))

# Slide 22

x = "Muhammad Abdullah"
print("Complete String: ", x)
print("Index String: ", x[0])
print("Index String: ", x[-5])
print("Slicing String: ", x[0:8])
print("Slicing String: ", x[-8:-1])
print("Slicing String: ", x[:8])
print("Slicing String: ", x[9:])

# Slide 22

a = "  Hello, Python!  "
print("Length is: ", len(a))

print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H","J"))

print("Python" in a)

# Slide 29

a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Slide 32

a=60
b=13
print("a=",bin(a),"\nb=",bin(b)) 
print("a&b=",bin(a&b))
print("a|b=",bin(a|b))
print("a^b=",bin(a^b))
print("a|b=",bin(a|b))
print("~a=",bin(~a))
print("a<<2=",bin(a<<2))
print("a>>b=",bin(a>>2))

# Slide 38

a = 10
if a%2 == 0:
    if a%5 == 0:
        print("Number is Divisible on Both 5 & 2")
if a == 11:
    print("Number is 11")
elif a == 10:
    print("Number is 10")
else:
    print("a is not present")

# Slide 43

def add(x,y,z=0):
    print("Addition is: ", x+y+z)
def mul(x,y,z=1):
    print("Multiplication is: ", x*y*z)
def div(x,y,z=1):
    print("Division is: ", x//y//z)

add(1,2,3)
mul(9,2,3)
div(1,2,3)