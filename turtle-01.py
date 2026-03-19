# Turtle Flower (Example)
# Draws flower patterns using a function and turtle graphics.

import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

def flower(rotations,angle,circle_size,distance):
  t.forward(distance)
  i=0
  while i<rotations:
    t.circle(circle_size)
    t.right(angle)
    i+=1
  t.goto(0,0)
  
flower(5,45,20,100)
flower(4,90,15,5)
