"""
Project Name: 
Author: Isaac Hill
Due Date: 10/9/2020
Course: CS1400-X04

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

This program when ran, will calculate how many months before running out of cages for rabbits and put it into
a table that will be created in a csv file. It will have the starting amount of pairs of rabbits and they will
have children and the children will grow up and then they have children in turn growing exponentially.
To change the starting values and stopping condition (cages) just changed them right at the
beginning of the main function.
"""


#Code starts here!
def main():
    
    #Sets up initial variables and stopping value (cages).
    cages = 500
    adults = 1
    babies = 0
    
    months = 1
    growingup = 0
    total = adults + babies
    f = open("rabbits.csv", 'w')
    
    #Writes the header and month 1 for the file.
    f.write("# Table of rabbit pairs\n")
    f.write("Month, Adults, Babies, Total\n")
    f.write("%s, %s, %s, %s\n" % (months, adults, babies, total))
    
    #Calculates each month while the total is less than the cages the adults, babies, and the total.
    while total < cages:
        months += 1
        growingup = babies
        babies = adults
        adults = adults + growingup
        total = adults + babies
        f.write("%s, %s, %s, %s\n" % (months, adults, babies, total))
        
    #Writes out when the cages will run out and closes file.
    f.write("# Cages will run out in month %s" % (months))
    f.close()    
        
if __name__ == "__main__":
    main()