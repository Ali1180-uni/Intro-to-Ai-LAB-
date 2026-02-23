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


# Question 4
# class book:
#     def __init__(self, ISBN, title, price, Main_Area, Sub_Area, no_of_pages):
#         self.ISBN = ISBN
#         self.title = title
#         self.price = price
#         self.Main_Area = Main_Area
#         self.Sub_Area = Sub_Area
#         self.no_of_pages = no_of_pages

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Price: ${self.price}")
#         print(f"ISBN: {self.ISBN}")
#         print(f"Main Area: {self.Main_Area}")
#         print(f"Sub Area: {self.Sub_Area}")
#         print(f"Number of Pages: {self.no_of_pages}")

# book1 = book("1291", "Python", 29, "Programming", "Python", 350)
# book1.display_info()