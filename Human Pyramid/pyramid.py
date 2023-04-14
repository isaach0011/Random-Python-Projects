"""
pyramid.py
Created by: Isaac Hill
Created on: 9/29/2021

This program takes how many rows to calculate from the command line. It then will for each row and column calculate the weight on each person's shoulders 
if they were standing on each other like a pyramid. This is done using recursion and stopping cases. To lessen the load on computers when calculating a high
number of rows, a cache is used. When the program is done calculating someone's weight on them, it will be saved to the cache so that if it needs to access
that weight later, the caculation doesn't need to be done again. (Reduces the function calls from 466 to 70 when calculating 7 rows.) When caculating these
values it will then print them. It also prints any information about the program such as how long it took, how many function calls there were, and how
many times the cache was accessed.

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""
import sys
from time import perf_counter

cache = {}
function_calls = 0
cache_hits = 0

def weight_on(r,c):
    global function_calls
    global cache_hits

    function_calls += 1

    #Checks cache for weight first before computing.
    if (r,c) in cache:
        cache_hits += 1
        return cache[(r,c)]
 
    #initialize weight to zero
    weight = 0
    #If row is lesser than (past the top) or equal to 0 (the top person) the weight on person's shoulder is 0.
    if r <= 0:
        weight = 0
    #If person is past pyramid, weight is 0.
    elif c < 0 or c > r:   
        weight = 0
    else:
        #If person is the right most on row, calculate the weight_on of person above and left of them and add the weight of the person above them then divide all by 2.
        if c == r:
            weight = (weight_on(r - 1,c - 1) + 200) / 2
        #If person is the left most on row, calculate the weight_on of person above them and add the weight of the person above them then divide all by 2.
        elif c == 0:
            weight = (weight_on(r - 1,c) + 200) / 2
        #If person is inbetween two people, calculate the weight on right shoulder and left shoulder and add those together.
        else:
            right_shoulder_weight = (weight_on(r - 1,c) + 200) / 2
            left_shoulder_weight = (weight_on(r - 1,c - 1) + 200) / 2
            weight = right_shoulder_weight + left_shoulder_weight
    #Save the weight to the cache for later use.
    cache[(r,c)] = weight
    return weight

def main():
    #Gets amount of rows from command line.
    rows = int(sys.argv[1])

    #Starts timer for timing how long recursion takes.
    start_time = perf_counter()

    #For writing to file.
    """
    with open('part3.txt', 'w') as part_three_file:
        for r in range(0, rows):
            for c in range(0, r + 1):
                part_three_file.write(f"{weight_on(r, c):0.2f} ")
            part_three_file.write("\n")

        part_three_file.write(f"Elapsed time: {perf_counter() - start_time} seconds\n")
        part_three_file.write(f"Number of function calls: {function_calls}\n")
        part_three_file.write(f"Number of cache hits: {cache_hits}")
    """

    #For printing to command line.
    for r in range(rows):
        for c in range(r + 1):
            #Prints weight on each person for each person in the row. Uses end=" " so no new line is made.
            print(f"{weight_on(r, c):0.2f}", end=" ")
        #Prints new line so new row is not on the same line
        print()

    #Gets the end time for timing how long recursion took.
    end_time = perf_counter()

    #Prints information.
    print(f"Elapsed time: {end_time - start_time} seconds")
    print(f"Number of function calls: {function_calls}")
    print(f"Number of cache hits: {cache_hits}")


if __name__ == "__main__":
    main()