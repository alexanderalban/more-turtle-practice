# Let's Make a Turtle!
# import turtle

import turtle
t = turtle.Pen()

# t.reset()
# for x in range(1, 5):
#     t.forward(50)
#     t.left(90)

# # and something more interesting

# t.reset()
# for x in range(1, 9):
#     t.forward(100)
#     t.left(225)

# # and again

# t.reset()
# for x in range(1, 38):
#     t.forward(100)
#     t.left(175)

# # sprials

# t.reset()
# for x in range(1, 20):
#     t.forward(100)
#     t.left(95)

# # you can also use if statements to make more complicated shapes

# t.reset()
# for x in range(1, 19):
#     t.forward(100)
#     if x % 2 == 0:
#         t.left(175)
#     else:
#         t.left(225)

# now let's draw a car- 

# t.reset()
# t.color(1,0,0)
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(20)
# t.left(90)
# t.forward(20)
# t.right(90)
# t.forward(20)
# t.left(90)
# t.forward(60)
# t.left(90)
# t.forward(20)
# t.right(90)
# t.forward(20)
# t.left(90)
# t.forward(20)
# t.end_fill()

# # Next, we draw the wheel

# t.color(0, 0, 0)
# t.up()
# t.forward(10)
# t.down()
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# # aaaaand the other one

# t.setheading(0)
# t.up()
# t.forward(90)
# t.right(90)
# t.forward(10)
# t.setheading(0)
# t.begin_fill()
# t.down()
# t.circle(10)
# t.end_fill()


# Coloring things in! the color function takes in three parameters: red, green, and blue. 
# Let's draw a yellow circle:

# t.reset
# t.color(1, 1, 0)
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# function to draw a filled circle

# def mycircle(red, green, blue):
#     t.reset()
#     t.color(red, green, blue)
#     t.begin_fill()
#     t.circle(50)
#     t.end_fill()

# mycircle(0, .5, 0)

# # A square drawing function


# def mysquare(size):
#     for x in range(1, 5):
#         t.forward(size)
#         t.left(90)

# t.reset()
# mysquare(100)


# t.reset()
# mysquare(25)
# mysquare(50)
# mysquare(75)
# mysquare(100)
# mysquare(125)

# # drawing a filled square

# t.reset()
# t.begin_fill()
# mysquare(50)
# t.end_fill()

# def myfancysquare(size, filled):
#     if filled == True:
#         t.begin_fill()
#     for x in range(1, 5):
#         t.forward(size)
#         t.left(90)
#     if filled == True:
#         t.end_fill()

# myfancysquare(50, True)
# myfancysquare(150, False)



# # Drawing filled stars 

# def mystar(size, filled):
#     if filled == True:
#         t.begin_fill()
#     for x in range(1, 19):
#         t.forward(size)
#         if x % 2 == 0:
#             t.left(175)
#         else:
#             t.left(225)
#     if filled == True:
#         t.end_fill()

# t.reset()
# t.color(0.9, 0.75, 0)
# mystar(120, True)


####### More practice!!!!

t.reset()

# Let's draw an octagon, filled and with an outline

def myoctagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()
    t.color(0, 0, 0,)
    for x in range(1, 9):
        t.forward(size)
        t.left(45)

t.color(1, 1, 0)
myoctagon(100, True)

input("just here to keep the window from closing")