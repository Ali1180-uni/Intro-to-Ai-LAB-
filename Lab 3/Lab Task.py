# Question 1
# class Add:
#     def __init__(self,a):
#         self.a = a
#     def __add__(self, o):
#         return self.a + o.a

# ob1 = Add(1.5)
# ob2 = Add(2.6)
# ob3 = Add("Lahore")
# ob4 = Add("Faisalabad")
# print(ob1 + ob2)
# print(ob3 + ob4)

# Question 2
# class A:
#     def __init__(self, a):
#         self.a = a
#     def __lt__(self, other):
#         if(self.a < other.a):
#             return "Less Than"
#         else:
#             return "Greater Than"
#     def __eq__(self, other):
#         if(self.a == other.a):
#             return "Both are Equal"
#         else:
#             return "Not Equal"

# ob1 = A(9)
# ob2 = A(6)
# print(ob1 < ob2)
# print(ob1 == ob2)

# Question 3
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printName(self):
#         print(self.fname, self.lname)

# class Student(Person):
#     pass

# x = Student("Ahmad", "Ali")
# x.printName()

# Question 4
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printName(self):
#         print(self.fname, self.lname)

# class Student(Person):
#     def __init__(self, fname, lname, graduationyear):
#         super().__init__(fname, lname)
#         self.graduationyear = graduationyear
#     def welcome(self):
#         print(f"Welcome {self.fname} {self.lname} to the class of {self.graduationyear}")

# x = Student("Shah", "Jahan", 2024)
# x.welcome()

# Question 5
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printName(self):
        print(f"Person Name: {self.fname} {self.lname}")

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def printName(self):
        super().printName()
        print(f"Student Graduation Year: {self.graduationyear}")

p = Person("Ayesha", "Sadia")
s = Student("Ahmad", "Ali", 2025)
p.printName()
s.printName()
