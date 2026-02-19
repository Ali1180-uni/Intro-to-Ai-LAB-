import turtle as t

# <---------- Shape Task ---------->
# t.pensize(3)
# t.color("red")
# t.penup()

# # Triangle
# t.goto(-200, -50)
# t.pendown()
# t.circle(40, steps=3)

# # Rectangle
# t.penup()
# t.goto(-100, -50)
# t.pendown()
# t.circle(40, steps=4)

# # Pentagon
# t.penup()
# t.goto(0, -50)
# t.pendown()
# t.circle(40, steps=5)

# t.done()

# <---------- Line Task ---------->

# x1,y1 = input("Enter the coordinates of the first point (x1, y1): ").split()
# x2,y2 = input("Enter the coordinates of the second point (x2, y2): ").split()

# x1, y1 = float(x1), float(y1)
# x2, y2 = float(x2), float(y2)

# distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# t.penup()
# t.goto(x1, y1)
# t.write("P1")
# t.pendown()
# t.goto(x2, y2)
# t.write("P2")
# t.penup()
# t.goto((x1+x2)/2, (y1+y2)/2)
# t.write(f"Distance: {distance}")
# t.hideturtle()
# t.done()


# <---------- Circle Radius Task ---------->


x1,y1 = input("Enter the coordinates of the first point (x1, y1): ").split()
x2,y2 = input("Enter the coordinates of the second point (x2, y2): ").split()
x3 = float(input("Enter the Radius of the circle: "))

x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
x, y = x1, y1 + x3
d = ((x2-x)**2 + (y2-y)**2)**0.5

t.pensize(3)
t.pencolor("blue")
t.penup()
t.goto(x1, y1)
t.pendown()
t.circle(x3)
t.penup()
t.goto(x2, y2)
t.begin_fill()
t.color("purple")
t.pendown()
t.circle(2)
t.goto(x2, y2+3)
t.write("P1")
t.end_fill()
t.penup()
t.goto(x1-x3, y1-x3)

if d < x3:
    t.write("The point is inside the circle.", font=("Arial", 12, "normal"))
else:
    t.write("The point is outside the circle.", font=("Arial", 12, "normal"))
t.hideturtle()
t.done()