from turtle import *
pencolor('white')
bgcolor('blue')
fillcolor('red')
setup(500,500)
speed(0)
angle=45
length=100
num_lines=8
hideturtle()
begin_fill()
for x in range(num_lines):
    left(angle)
    forward(length)
############################
penup()
left(20)
goto(-50,120)
pendown()
write('STOP',move=False,align='center',font=('Ariel',25,'bold'))
end_fill()
done()