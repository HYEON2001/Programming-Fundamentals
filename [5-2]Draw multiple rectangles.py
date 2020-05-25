import turtle as t

def draw_square(a, size):
    for _ in range(4):
        a.forward(size)
        a.left(90)


window = t.Screen()
alex = t.Turtle()
alex.speed(50)
boxes = 20
for _ in range(boxes):
    draw_square(alex, 200)
    alex.left(360 / boxes)
window.mainloop()
