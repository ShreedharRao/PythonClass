from turtle import *

i = 1
pendown()
pensize(5)
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(75)
    if abs(pos()) < 1:
        break
end_fill()
done()