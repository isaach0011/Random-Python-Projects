"""
Project Name: Random Walk
Author: Isaac Hill
Due Date: 12/4/2020
Course: CS1400-X04

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

The program will simulate what "Pa", "MiMa" and "Reg" would walk and gives information about
that simulation such as mean, max, min and Coefficient of Variance. When it starts you will
give a list of the amount of steps you would like them to walk either one number or multiple
typed like "100,1000" then asked about the amount of trials or time you want them to do this.
Finally you will be asked about who you want to simulate walking. Then the program will calculate
walking and give information about each step set. Then the program will use turtle to make
a graph showing where the end points of each trial for a 100 step set and change the icon
for who walked. Red Arrow = Reg   Black Circle = Pa   Green Square = MiMa
"""

import turtle
import random
import statistics

def main():
    
    #Asks user for how many steps, trials, and who is walking
    steps = input("What is a list of walk lengths you want to simulate? (use commas to seperate the numbers) ")
    
    #If ValueError happens prints message and exits.
    try:
        trials = int(input("How many tries of the walk lengths do you want to do? "))
    except ValueError:
        print("Invalid option: Restart program and use a whole number for trials.")
        exit()
        
    typeOfWalk = input("What type of walk model? (Pa, MiMa, Reg, or All) ")
    
    #If not valid option prints message and exits.
    if typeOfWalk != "Pa" and typeOfWalk != "MiMa" and typeOfWalk != "Reg" and typeOfWalk != "All":
        print("Invalid option: Restart program and select valid option.")
        exit()
    
    #Changes items in list to integers and if error happens prints message and exits.
    stepList = steps.split(",")
    for i in range(0, len(stepList)):
        try:
            stepList[i] = int(stepList[i])
        except ValueError:
            print("Invalid option: Restart program and use a whole numbers for step list.")
            exit()
    
    #Sets up Turtle and runs walking simulation
    t = setup()
    if typeOfWalk == "All":
        for i in range(0, len(stepList)):
            walkSimulation(t, stepList[i], trials, "Pa", "no")
        for i in range(0, len(stepList)):
            walkSimulation(t, stepList[i], trials, "MiMa", "no")
        for i in range(0, len(stepList)):
            walkSimulation(t, stepList[i], trials, "Reg", "no")
    else:
        for i in range(0, len(stepList)): 
            walkSimulation(t, stepList[i], trials, typeOfWalk, "no")
              
    #Creates plot graph for 50 trials using 100 steps
    walkSimulation(t, 100, 50, "Pa", "yes")
    walkSimulation(t, 100, 50, "MiMa", "yes")
    walkSimulation(t, 100, 50, "Reg", "yes")

#Takes the turtle, steps, trials, who is walking, and if its running a graph
def walkSimulation(t, steps, trials, walkType, graph):
    turns = [0,90,180,270]
    RegTurns = [0,180]
    
    PaNumbers = []
    MiMaNumbers = []
    RegNumbers = []
    
    #For each trial and each step run a random number generator to decide a direction
    for _ in range(trials):
        for _ in range(steps):
            if walkType == "Reg":
                t.left(random.choice(RegTurns))
                t.penup()
                if graph == "yes":
                    t.forward(9)
                else:
                    t.forward(1)
            elif walkType == "Pa":
                t.left(random.choice(turns))
                t.penup()
                if graph == "yes":
                    t.forward(9)
                else:
                    t.forward(1)
            elif walkType == "MiMa":
                t.left(random.choice(turns))
                if t.heading() == 270:
                    t.penup()
                    if graph == "yes":
                        t.forward(18)
                    else:
                        t.forward(2)   
                else:
                    t.penup()
                    if graph == "yes":
                        t.forward(9)
                    else:
                        t.forward(1)
     
        #When it reaches the end of walking stamps and icon on a graph for its end location
        if walkType == "Reg":
            if graph == "yes":
                stampReg(t)
                reset(t)
            else:
                RegNumbers.append(t.distance(0,0))
                t.home()
                t.setheading(0)

        elif walkType == "Pa":
            if graph == "yes":
                stampPa(t)
                reset(t)
            else:
                PaNumbers.append(t.distance(0,0))
                t.home()
                t.setheading(0)
                
        elif walkType == "MiMa":
            if graph == "yes":
                stampMiMa(t)
                reset(t)
            else:
                MiMaNumbers.append(t.distance(0,0))
                t.home()
                t.setheading(0)
                
    #If its not being ran as a graph it prints the mean, CV, max, and the min.
    if walkType == "Pa" and graph == "no":
        print("Pa random walk of", steps, "steps")
        print(f"Mean = {round(statistics.mean(PaNumbers), 1)} CV = {round(statistics.stdev(PaNumbers)/statistics.mean(PaNumbers), 1)}")
        print(f"Max = {round(max(PaNumbers),1)} Min = {round(min(PaNumbers),1)}\n")
        
    elif walkType == "MiMa" and graph == "no":
        print("Mi-Ma random walk of", steps, "steps")
        print(f"Mean = {round(statistics.mean(MiMaNumbers), 1)} CV = {round(statistics.stdev(MiMaNumbers)/statistics.mean(MiMaNumbers), 1)}")
        print(f"Max = {round(max(MiMaNumbers),1)} Min = {round(min(MiMaNumbers),1)}\n")
        
    elif walkType == "Reg" and graph == "no":
        print("Reg random walk of", steps, "steps")
        print(f"Mean = {round(statistics.mean(RegNumbers), 1)} CV = {round(statistics.stdev(RegNumbers)/statistics.mean(RegNumbers), 1)}")
        print(f"Max = {round(max(RegNumbers),1)} Min = {round(min(RegNumbers),1)}\n")
  
#Stamps a black circle where the turtle is
def stampPa(t):
    t.pendown()
    t.color("black")
    t.shape("circle")
    t.stamp()
  
#Stamps a green square where the turtle is
def stampMiMa(t):
    t.pendown()
    t.color("green")
    t.shape("square")
    t.stamp()

#Stamps a red triangle where the trutle is
def stampReg(t):
    t.pendown()
    t.setheading(0)
    t.color("red")
    t.shape("triangle")
    t.stamp()

#sets the turtle to go to (0,0) and changes angle to 0
def reset(t):
    t.penup()
    t.home()
    t.setheading(0)
 
#Sets up turtle
def setup():
    t = turtle.Turtle()
    turtle.tracer(0)
    return t
 
if __name__ == "__main__":
    main()
