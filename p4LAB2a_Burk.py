import turtle
win = turtle.Screen()
win.title("Alex & Tess")

alex = turtle.Turtle()
alex.color("blue")
for i in range(4):
    alex.forward(50)
    alex.left(90)


tess = turtle.Turtle()
tess.color("hotpink")
for x in range(3):
    tess.forward(100)
    tess.left(120)


win.mainloop()
