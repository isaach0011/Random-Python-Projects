"""
Project Name: 
Author: Isaac Hill
Due Date: 09/25/2020
Course: CS1400-X04

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

This program uses turtle to create a scene of a landscape. Function create shapes
and other functions place those shapes in specific ways to create the scene.
I learned that it took a lot of trial and error and very fine tuning to get the
shapes in the right place and to reset the heading so that everything isn't
rotated.

"""
import turtle

# Starts here
def main():
    t = setup()
    grass(t)
    clouds(t)
    sun(t)
    sunRays(t)
    mountains(t)
    trees(t)
    lake(t)
    dock(t)
    boat(t)

# This method sets up turtle and the window
def setup():
    t = turtle.Turtle()
    turtle.tracer(0)
    t.speed(0)
    t.pensize(3)
    turtle.setup(1000, 800)
    turtle.bgcolor("cyan")
    t.up()
    return t

#draws boat using and upside down trapezoid
def boat(t):
    t.goto(-50, -250)
    draw_trapezoid(t, "brown", "saddle brown", 40, 30, 70)
    
#draws dock using rectangles
def dock(t):
    t.goto(165, -215)
    draw_rectangle(t, "saddle brown", "peru", 15, 40)
    t.goto(150, -215)
    draw_rectangle(t, "saddle brown", "peru", 15, 40)
    t.goto(135, -215)
    draw_rectangle(t, "saddle brown", "peru", 15, 40)
    t.goto(120, -215)
    draw_rectangle(t, "saddle brown", "peru", 15, 40)
    t.goto(105, -215)
    draw_rectangle(t, "saddle brown", "peru", 15, 40)
    t.goto(90, -215)
    draw_rectangle(t, "saddle brown", "peru", 15, 40)
    
    
#draws lake using 3 blue circles
def lake(t):
    t.goto(50, -325)
    draw_circle(t, "royal blue", "royal blue", 125)
    t.goto(-100, -300)
    draw_circle(t, "royal blue", "royal blue", 100)
    t.goto(-50, -375)
    draw_circle(t, "royal blue", "royal blue", 75)


#draws trees with green triangles and brown rectangles
def trees(t):
    #draws trunks
    t.goto(218, -110)
    draw_rectangle(t, "saddle brown", "sienna", 15, 35)
    t.goto(-415, -225)
    draw_rectangle(t, "saddle brown", "sienna", 30, 75)
    t.goto(355, -385)
    draw_rectangle(t, "saddle brown", "sienna", 45, 85)
    t.goto(-330, -445)
    draw_rectangle(t, "saddle brown", "sienna", 60, 95)
    
    #draws toppers
    t.goto(200, -75)
    draw_triangle(t, "dark green", "green", 50, 120)
    t.goto(-450, -150)
    draw_triangle(t, "dark green", "green", 100, 120)
    t.goto(300, -300)
    draw_triangle(t, "dark green", "green", 150, 120)
    t.goto(-400, -350)
    draw_triangle(t, "dark green", "green", 200, 120)
    
#draws yellow sun
def sun(t):
    #sun
    t.goto(435, 285)
    draw_circle(t, "orange", "yellow", 50)
    
#draws rectangular rays around the sun
def sunRays(t):
    t.goto (430, 205)
    draw_rectangle(t, "orange", "yellow", 10, 60)
    t.setheading(-30)
    t.goto (355, 225)
    draw_rectangle(t, "orange", "yellow", 10, 60)
    t.setheading (-65)
    t.goto (310, 285)
    draw_rectangle(t, "orange", "yellow", 10, 60)
    t.setheading (-110)
    t.goto (315, 380)
    draw_rectangle(t, "orange", "yellow", 10, 60)
    
    t.setheading(0)
    
    
#draws gray mountains using 3 connected triangles
def mountains(t):
    t.goto(-400, 0)
    draw_triangle(t, "dim gray", "gray", 250, 120)
    t.goto(-300,0)
    draw_triangle(t, "dim gray", "gray", 200, 120)
    t.goto(-200,0)
    draw_triangle(t, "dim gray", "gray", 300, 120)

#draws white clouds using 3 circles connected
def clouds(t):
    #draws clouds on left side
    t.goto(-400, 200)
    draw_circle(t, "white", "white", 50)
    t.goto(-350, 225)
    draw_circle(t, "white", "white", 60)
    t.goto(-275, 225)
    draw_circle(t, "white", "white", 50)
    
    #draws clouds on rigth side
    t.goto(300, 100)
    draw_circle(t, "white", "white", 50)
    t.goto(250, 125)
    draw_circle(t, "white", "white", 60)
    t.goto(175, 125)
    draw_circle(t, "white", "white", 50)
    
#draws lime green grass
def grass(t):
    t.goto(-500, -400)
    draw_rectangle(t, "lime green", "lime green", 1000, 400)
    
#draws a circle usuing the pen color, fill, and size
def draw_circle(t, pen_color, fill_color, size):
    t.down()
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.up()

#draws a triangle using the pen color, fill, size and angle
def draw_triangle(t, pen_color, fill_color, side, angle):
    t.down()
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side)
        t.left(angle)
    t.end_fill()
    t.up()

#draws a rectangle using the pen color, fill, and the side lengths
def draw_rectangle(t, pen_color, fill_color, short_side, long_side):
    t.down()
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(short_side)
        t.left(90)
        t.forward(long_side)
        t.left(90)
    t.end_fill()
    t.up()

#draws a trapezoid using the pen color, fill, and the lengths of the sides
def draw_trapezoid(t, pen_color, fill_color, bottom, side, top):
    t.down()
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.forward(bottom)
    t.left(60)
    t.forward(side)
    t.left(120)
    t.forward(top)
    t.left(120)
    t.forward(side)
    t.left(60)
    t.end_fill()
    t.up()
    
if __name__ == "__main__":
    main()