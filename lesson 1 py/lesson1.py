from turtle import *

#we want to paint a hause

#step 1:  draw a square
speed(200)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door


color("blue")
begin_fill()
forward(70)
left(90)
forward(120)          #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()




penup()
goto(150,150)
pendown()


color("brown")
begin_fill()
forward(70)
left(90)
forward(70)
left(70)
forward(70)
left(70)
forward(90)
end_fill()




exitonclick()