import turtle as t

def star(turtle_obj, N):
    for _ in range(5):
        turtle_obj.forward(N/3)
        turtle_obj.right(144)

    turtle_obj.penup()
    turtle_obj.forward(N)
    turtle_obj.right(144)
    turtle_obj.pendown()


window = t.Screen()
alex = t.Turtle()
for i in range(5):
    star(alex, 200)
window.mainloop()
