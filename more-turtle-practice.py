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

t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()

# Next, we draw the wheel

t.color(0, 0, 0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

# aaaaand the other one

t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

input("just here to keep the window from closing")