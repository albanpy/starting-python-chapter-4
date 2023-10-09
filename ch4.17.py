from turtle import *
#Star Pattern
angle=135
length=200
bgcolor('cyan')
pencolor('white')
fillcolor('white')
begin_fill()
speed(0)
for i in range(8):
    left(angle)
    forward(200)
hideturtle()
end_fill()
done()
