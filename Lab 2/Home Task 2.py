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

