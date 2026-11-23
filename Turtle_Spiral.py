from _tkinter import *
import turtle

# Set up the screen window
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.shape("turtle")


colors = ["red", "green", "blue"]
for i in range(40):
    t.forward(30 + i)
    t.left(40 - i / 1.5)
    t.color(colors[i % 3])

turtle.done()
