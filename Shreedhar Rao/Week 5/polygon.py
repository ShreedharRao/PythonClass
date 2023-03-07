#This is a project to make any polygon using Turtle
from turtle import *
import random

def square(length):
    i = 0
    while i< 4:
        forward(length)
        left(90)
        i=i+1

def polygon(length, sides):
    if sides < 3:
        return
    i = 0
    while i < sides:
        forward(length)
        left(360/sides)
        i = i + 1

#square(200)

#polygon(5,150)

#polygon(6,100)

#polygon(7,50)

s= int(input("enter number of sides: "))
l= int(input("enter length of sides: "))
polygon(l,s)
done()