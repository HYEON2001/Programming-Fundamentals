import turtle as t
window=t.Screen()
alex=t.Turtle()
length = 10
alex.speed(30)
for _ in range(30):
    alex.forward(length)
    alex.right(90)
    alex.forward(length)
    alex.right(90)
    length+=5
window.mainloop()
