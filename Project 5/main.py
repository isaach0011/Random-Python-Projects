"""
Project Name: 
Author: Isaac Hill
Due Date: 11/13/2020
Course: CS1400-X04

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

This program uses turtle to create a scene of a landscape. Function create shapes
and other functions place those shapes in specific ways to create the scene. When
the program starts the user has the option between 3 scenes and just type the
number in. Option 1 is a morning scene. Option 2 is an afternoon scene.
Option 3 is an evening scene.
"""
import turtle
import random

# Starts here
def main():
    scene = int(input("What time of day do you want?(Type a number 1-3)\n1: Morning" +
        "\n2: Afternoon\n3: Evening\n"))
    if scene == 1 or scene == 2 or scene == 3:
        drawScene(scene)
    else:
        print("Invalid option. Choose a valid option 1-3.")
        exit()

#Draws scene
def drawScene(option):
    t = setup(option)
    scale = 1
    
    #Runs drawing the scene twice
    for i in range(2):
        #Draws the camera only the second time ran.
        if i == 1:
            camera(t, option)
            
        grass(t, scale)
        #If evening option draws stars and moon
        if option == 3:
            stars(t, scale)
            moon(t, scale)
        #If morning or afternoon draws clouds and sun
        if option == 1 or option == 2:
            clouds(t, scale)
            sun(t, scale, option)
        #If afternoon draws sun rays
        if option == 2:
            sunRays(t, scale)
        mountains(t, scale)
        house(t, scale)
        trees(t, scale)
        lake(t, scale)
        dock(t, scale)
        boat(t, scale)
        
        #Changes the scale to make the second drawing smaller
        scale = .3

# This method sets up turtle and the window
def setup(option):
    t = turtle.Turtle()
    turtle.tracer(0)
    t.speed(0)
    t.pensize(3)
    turtle.setup(1000, 800)
    #Changes background color based on selection of scene
    if option == 1:
        turtle.bgcolor("orange")
    elif option == 2:
        turtle.bgcolor("cyan")
    elif option == 3:
        turtle.bgcolor("dark slate blue")
    t.up()
    return t

#draws camera around the second scene
def camera(t, option):
    #draws camera and buttons
    t.goto(-175, -145)
    draw_rectangle(t, "black", "dim gray", 350, 290)
    t.goto(120, 145)
    draw_rectangle(t, "black", "dim gray", 40, 15)
    t.goto(-185, 70)
    draw_rectangle(t, "black", "dim gray", 10, 40)
    t.goto(-185, 20)
    draw_rectangle(t, "black", "dim gray", 10, 40)
    
    #draws camera mount and stand
    t.goto(-100, -165)
    draw_rectangle(t, "black", "dim gray", 200, 20)
    t.goto(-15, -320)
    draw_rectangle(t, "black", "dim gray", 30, 155)
    t.setheading(-40)
    t.goto(-110, -420)
    draw_rectangle(t, "black", "dim gray", 30, 155)
    t.setheading(40)
    t.goto(90, -440)
    draw_rectangle(t, "black", "dim gray", 30, 155)
    t.goto(20, -330)
    draw_circle(t, "black", "dim gray", 30)
    
    t.setheading(0)
    #draws background for the second scene
    t.goto(-150, -120)
    if option == 1:
        draw_rectangle(t, "orange", "orange", 300, 240)
    elif option == 2:
        draw_rectangle(t, "cyan", "cyan", 300, 240)
    elif option == 3:
        draw_rectangle(t, "dark slate blue", "dark slate blue", 300, 240)
    
#draws boat using and upside down trapezoid
def boat(t, scale):
    t.goto(-50 * scale, -250 * scale)
    draw_trapezoid(t, "brown", "saddle brown", 40 * scale, 30 * scale, 70 * scale)
    
#draws dock using rectangles
def dock(t, scale):
    t.goto(165 * scale, -215 * scale)
    draw_rectangle(t, "saddle brown", "peru", 15 * scale, 40 * scale)
    t.goto(150 * scale, -215 * scale)
    draw_rectangle(t, "saddle brown", "peru", 15 * scale, 40 * scale)
    t.goto(135 * scale, -215 * scale)
    draw_rectangle(t, "saddle brown", "peru", 15 * scale, 40 * scale)
    t.goto(120 * scale, -215 * scale)
    draw_rectangle(t, "saddle brown", "peru", 15 * scale, 40 * scale)
    t.goto(105 * scale, -215 * scale)
    draw_rectangle(t, "saddle brown", "peru", 15 * scale, 40 * scale)
    t.goto(90 * scale, -215 * scale)
    draw_rectangle(t, "saddle brown", "peru", 15 * scale, 40 * scale)
    
    
#draws lake using 3 blue circles
def lake(t, scale):
    t.goto(50 * scale, -325 * scale)
    draw_circle(t, "royal blue", "royal blue", 125 * scale)
    t.goto(-100 * scale, -300 * scale)
    draw_circle(t, "royal blue", "royal blue", 100 * scale)
    t.goto(-50 * scale, -375 * scale)
    draw_circle(t, "royal blue", "royal blue", 75 * scale)

#Draws house using brown rectangles and trapezoid and a white square
def house(t, scale):
    #draws house
    t.goto(250 * scale, -200 * scale)
    draw_rectangle(t, "saddle brown", "peru", 150 * scale, 20 * scale)
    t.goto(250 * scale, -180 * scale)
    draw_rectangle(t, "saddle brown", "peru", 150 * scale, 20 * scale)
    t.goto(250 * scale, -160 * scale)
    draw_rectangle(t, "saddle brown", "peru", 150 * scale, 20 * scale)
    t.goto(250 * scale, -140 * scale)
    draw_rectangle(t, "saddle brown", "peru", 150 * scale, 20 * scale)
    t.goto(250 * scale, -120 * scale)
    draw_rectangle(t, "saddle brown", "peru", 150 * scale, 20 * scale)
    t.goto(250 * scale, -100 * scale)
    draw_rectangle(t, "saddle brown", "peru", 150 * scale, 20 * scale)
    
    #draws door
    t.goto(270 * scale, -200 * scale)
    draw_rectangle(t, "saddle brown", "sienna", 50 * scale, 80 * scale)
    
    #draws window
    t.goto(340 * scale, -160 * scale)
    draw_rectangle(t, "gray", "white", 40 * scale, 40 * scale)
    
    #draws roof
    t.goto(425 * scale, -80 * scale)
    draw_trapezoid(t, "saddle brown", "sienna", -205 * scale, 40 * scale, -165 * scale)
    
#draws trees with green triangles and brown rectangles
def trees(t, scale):
    #draws trunks
    t.goto(-218 * scale, -110 * scale)
    draw_rectangle(t, "saddle brown", "sienna", 15 * scale, 35 * scale)
    t.goto(-415 * scale, -225 * scale)
    draw_rectangle(t, "saddle brown", "sienna", 30 * scale, 75 * scale)
    t.goto(355 * scale, -385 * scale)
    draw_rectangle(t, "saddle brown", "sienna", 45 * scale, 85 * scale)
    t.goto(-330 * scale, -405 * scale)
    draw_rectangle(t, "saddle brown", "sienna", 60 * scale, 65 * scale)
    
    #draws toppers
    t.goto(-235 * scale, -75 * scale)
    draw_triangle(t, "dark green", "green", 50 * scale, 120)
    t.goto(-450 * scale, -150 * scale)
    draw_triangle(t, "dark green", "green", 100 * scale, 120)
    t.goto(300 * scale, -300 * scale)
    draw_triangle(t, "dark green", "green", 150 * scale, 120)
    t.goto(-400 * scale, -350 * scale)
    draw_triangle(t, "dark green", "green", 200 * scale, 120)
    
#draws yellow sun
def sun(t, scale, option):
    #If morning draws sun lower
    if option == 1:
        t.goto(435 * scale, 10 * scale)
        draw_circle(t, "orange", "yellow", 50 * scale)
    #If afternoon draws sun higher
    elif option == 2:
        t.goto(435 * scale, 285 * scale)
        draw_circle(t, "orange", "yellow", 50 * scale)
        
    
#draws rectangular rays around the sun
def sunRays(t, scale):
    t.goto (430 * scale, 205 * scale)
    draw_rectangle(t, "orange", "yellow", 10 * scale, 60 * scale)
    t.setheading(-30)
    t.goto (355 * scale, 225 * scale)
    draw_rectangle(t, "orange", "yellow", 10 * scale, 60 * scale)
    t.setheading (-65)
    t.goto (310 * scale, 285 * scale)
    draw_rectangle(t, "orange", "yellow", 10 * scale, 60 * scale)
    t.setheading (-110)
    t.goto (315 * scale, 380 * scale)
    draw_rectangle(t, "orange", "yellow", 10 * scale, 60 * scale)
    
    t.setheading(0)

#draws moon with white circle 
def moon(t, scale):
    t.goto(20 * scale, 285 * scale)
    draw_circle(t, "dark gray", "white", 50 * scale)
    t.goto(40 * scale, 285 * scale)
    draw_circle(t, "dark slate blue", "dark slate blue", 40 * scale)

#draws a random number of stars in random positions
def stars(t, scale):
    for _ in range(random.randint(0, 50)):
        t.goto(random.randint(-450 * scale, 450 * scale), random.randint(0, 350 * scale))
        draw_circle(t, "yellow", "white", 7 * scale)
    
#draws gray mountains using 3 connected triangles
def mountains(t, scale):
    t.goto(-400 * scale, 0)
    draw_triangle(t, "dim gray", "gray", 250 * scale, 120)
    t.goto(-300 * scale,0)
    draw_triangle(t, "dim gray", "gray", 200 * scale, 120)
    t.goto(-200 * scale,0)
    draw_triangle(t, "dim gray", "gray", 300 * scale, 120)

#draws white clouds using 3 circles connected
def clouds(t, scale):
    #draws clouds on left side
    t.goto(-400 * scale, 200 * scale)
    draw_circle(t, "white", "white", 50 * scale)
    t.goto(-350 * scale, 225 * scale)
    draw_circle(t, "white", "white", 60 * scale)
    t.goto(-275 * scale, 225 * scale)
    draw_circle(t, "white", "white", 50 * scale)
    
    #draws clouds on rigth side
    t.goto(300 * scale, 100 * scale)
    draw_circle(t, "white", "white", 50 * scale)
    t.goto(250 * scale, 125 * scale)
    draw_circle(t, "white", "white", 60 * scale)
    t.goto(175 * scale, 125 * scale)
    draw_circle(t, "white", "white", 50 * scale)
    
#draws lime green grass
def grass(t, scale):
    t.goto(-500 * scale, -400 * scale)
    draw_rectangle(t, "lime green", "lime green", 1000 * scale, 400 * scale)
    
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
