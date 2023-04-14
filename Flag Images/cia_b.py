"""
flags_b.py
Created by: Isaac Hill
Created on: 4/7/21
Last updated on: 4/8/21

Description:

Function available:
    downloadFlag(country):

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""
import requests
import os.path
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

link = "https://www.sciencekids.co.nz/images/pictures/flags680/"
size = 0

#Grabs all country names from flags.txt and puts them in a list
with open("flags.txt") as flagListFile:
    flags = flagListFile.read().splitlines()

def downloadFlag(country):
    """
    This function will create a file name to download from the website in the link variable and get the content from the flag link. It will then
    download the file and create a .jpg image with the countries name. Returns the size of the file.
    Parameters:
        country (str) : country to get flag from. (Case Sensitive)

    Returns:
        len(flag) (int) : returns the size of the file downloaded
    """
    fileName = link + country + ".jpg"
    #Gets content of the file from the site
    flag = requests.get(fileName).content
    with open(f"flags/{country}.jpg","wb") as pic:
        #Creates a file with content from the site
        pic.write(flag)
    return len(flag)

if __name__ == "__main__":
    startTime = perf_counter()
    #Seperates the fuction to run on different processes to increase speed
    with ProcessPoolExecutor(cpu_count()) as p:
        sizeTotal = sum(p.map(downloadFlag,flags))
    endTime = perf_counter()
    with open("cia_b_output.txt", "w") as outFile:
        outFile.write(f"Elapsed time: {endTime - startTime}\n")
        outFile.write(f"{sizeTotal} bytes downloaded")