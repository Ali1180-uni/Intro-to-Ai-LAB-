class person:
    name = "Ali"
    def __init__(self, age = 10):
        self.age = age
        self.__info = "10"
    def greet(self):
        return "Ali is a Good Boy"
    def getInfo(self):
        return self.__info
        
Ali = person()
print(Ali.age, Ali.name)
get = Ali.greet()
print(get)
print(Ali.getInfo())

class Student(person):
    def __init__(self, age):
        super().__init__(self.name)

hi = Student(20)
print(hi.name)
print(hi.greet())