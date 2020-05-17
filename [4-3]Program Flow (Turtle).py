import turtle as t
window=t.Screen()
alex = t.Turtle()
alex.shape("turtle")

for _ in range(12):
    alex.penup()
    alex.forward(80)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(30)
    alex.stamp()
    alex.backward(120)
    alex.right(30)

window.mainloop()
