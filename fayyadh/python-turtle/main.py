from turtle import *

getscreen()
shape("turtle")
bgcolor("gold")

pendown()
pencolor("red")
pensize(5)
speed(0)

init_size = 5
for i in range(50):
    for i in range(3):
      forward(100)
      left(120)
      init_size += 10
    left(7)  


penup()

done()