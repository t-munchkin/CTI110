import turtle
wn = turtle.Screen()
wn.title("Initials")

tb = turtle.Turtle()
tb.color("purple")
tb.pensize("8")

tb.penup()
tb.forward(120)
tb.right(90)
tb.pendown()
tb.forward(100)
tb.back(100)
tb.left(90)
tb.forward(40)
tb.bk(80)
tb.penup()
tb.forward(110)
tb.pendown()

tb.circle(35,180)
tb.left(90)
tb.forward(140)
tb.left(90)
tb.circle(35,180)


wn.mainloop()
