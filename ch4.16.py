#Turtle Graphics: Repeating Squares
from turtle import *
hideturtle()
speed(0)
setup(700,700)
L=10
L1=-10
num_square=50
incrL=4
##########
for i in range(num_square):
    goto(0,L)
    goto(L1,L)
    goto(L1,0)
    goto(0,0)
    ###################
    L+=incrL
    L1-=incrL 
done()