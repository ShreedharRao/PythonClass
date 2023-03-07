from turtle import *

i = 1
pendown()
pensize(5)
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(135)
    if abs(pos()) < 1:
        break
end_fill()

penup()
goto(-200, -100)
color("blue","red")
pendown()
counter=0
begin_fill()
while counter < 8:
    forward(200)
    left(135)
    counter=counter+1
end_fill()
done()