# Question 1
class Add:
    def __init__(self,a):
        self.a = a
    def __add__(self, o):
        return self.a + o.a

ob1 = Add(1.5)
ob2 = Add(2.6)
ob3 = Add("Lahore")
ob4 = Add("Faisalabad")
print(ob1 + ob2)
print(ob3 + ob4)