import os
import turtle
import time
import random

delay = 0.1

#ekran
wn = turtle.Screen()
wn.title(" Gra Snake ")
wn.bgcolor("#8061ad")
wn.setup(width=600, height=600)
wn.tracer(0)



#głowa węża

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#6ad486")
head.penup()
head.goto(0,0)
head.direction = ""

#jedzonko

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#961717")
food.penup()
food.goto(0,100)

segments = []

#funkcje
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)


    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
#bindy
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_down, "s")

#main loop
while True:
    
    
    wn.update()

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("#4c8f2e")
    new_segment.penup()
    segments.append(new_segment)

    for index in range(len(segments) -1, 0 ,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)

    wn.mainloop()
