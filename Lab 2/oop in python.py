import turtle as t
# <---------- Basic Task ---------->

# class dog:
#     attr1 = "mammal"
#     attr2 = "dog"
#     def fun(self):
#         print("i am a", self.attr1)
#         print("i am a", self.attr2)
# Roger = dog()
# print(Roger.attr1)
# Roger.fun()

# <---------- Basic Task ---------->

class Circle:
    def __init__(self, r=0, s=0, t=3):
        self.x = r
        self.y = s
        self.radius = t
    def drawCircle(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.radius)
        t.hideturtle()
        t.done()

c1 = Circle(0, 0, 50)
c1.drawCircle()