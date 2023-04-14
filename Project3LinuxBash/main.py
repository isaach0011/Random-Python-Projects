"""
main.py
Created by: Isaac Hill
Created on: 10/4/2021

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""

import re

def main():
  fileOneContent = ""
  fileTwoContent = ""
  #Open both files
  with open("PATH/file1.txt") as fileOne:
     with open("PATH/file2.txt") as fileTwo:
       #Grab file content
       fileOneContent = fileOne.read()
       fileTwoContent = fileTwo.read()

       #Reverse contents of file 1
       fileOneReverse = fileOneContent[::-1]

       #Create file3.txt and write the reversed content of file 1 to it
       with open("PATH/file3.txt", "w") as fileThree:
         fileThree.write(fileOneReverse)
       
       #Letter Changer
       fileTwoRemix = ""
       for letter in fileTwoContent:
         if letter == "a":
           fileTwoRemix += "b"
         elif letter == "c":
           fileTwoRemix += "d"
         elif letter == "e":
           fileTwoRemix += "f"
         elif letter == "g":
           fileTwoRemix += "h"
         elif letter == "i":
           fileTwoRemix += "j"
         elif letter == "k":
           fileTwoRemix += "l"
         elif letter == "m":
           fileTwoRemix += "n"
         elif letter == "o":
           fileTwoRemix += "p"
         elif letter == "q":
           fileTwoRemix += "r"
         elif letter == "s":
           fileTwoRemix += "t"
         elif letter == "u":
           fileTwoRemix += "v"
         elif letter == "w":
           fileTwoRemix += "x"
         elif letter == "y":
           fileTwoRemix += "z"
         elif letter == "A":
           fileTwoRemix += "B"
         elif letter == "C":
           fileTwoRemix += "D"
         elif letter == "E":
           fileTwoRemix += "F"
         elif letter == "G":
           fileTwoRemix += "H"
         elif letter == "I":
           fileTwoRemix += "J"
         elif letter == "K":
           fileTwoRemix += "L"
         elif letter == "M":
           fileTwoRemix += "N"
         elif letter == "O":
           fileTwoRemix += "P"
         elif letter == "Q":
           fileTwoRemix += "R"
         elif letter == "S":
           fileTwoRemix += "T"
         elif letter == "U":
           fileTwoRemix += "V"
         elif letter == "W":
           fileTwoRemix += "X"
         elif letter == "Y":
           fileTwoRemix += "Z"
         else:
           fileTwoRemix += letter

       #Split at x and X
       fileTwoList = re.split("x|X", fileTwoRemix)
       
       #Print list and then prints list items individually
       print(fileTwoList)
       for item in fileTwoList:
         print(item)
         
if __name__ == "__main__":
    main()