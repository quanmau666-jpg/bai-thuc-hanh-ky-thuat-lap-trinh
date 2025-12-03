import turtle

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("white")

colors = ["red", "blue", "green"]

n = 36  

for i in range(n):
    t.color(colors[i % 3])
    t.circle(80)
    t.left(360 / n)

turtle.done()
