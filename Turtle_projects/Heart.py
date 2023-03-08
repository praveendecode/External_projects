import math

from turtle import *



you = lambda k:12*math.sin(k)**3


me = lambda k: 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

speed(0)

bg("black")

for i in range(6000):
    goto(you(i)*20,me(i)*20)
    for j in range(1):
        color("red")
    goto(0,0)

done()
