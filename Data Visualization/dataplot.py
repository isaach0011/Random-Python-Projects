"""
dataplot.py
Created by: Isaac Hill
Created on: 11/19/21

Description: This program will load the data into the analyze function passed through the parameter into an ndarray called rawArray. It will then create a copy of that ndarray called smoothArray
    where the function will then smooth out the data using the formula. (yi-3 + 2yi-2 + 3yi-1 + 3yi + 3yi+1 + 2yi+2 + yi+3) / 15 The analyze function will then find pulses in the smoothArray and 
    put those in a list pulses. Then analyze will get the pulse area from each of the pulses and put those in another list called pulsesArea. It will then output a *.out file based on the name with the pulse
    and the area of the pulse. Then the function will create *.pdf with the graphs of the data. It will do this for each .dat file in the folder for where this program is in.

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""
import numpy as np
import glob
import matplotlib.pyplot as plt

def analyze(fileName):
    rawArray = np.loadtxt(fileName,'i')
    smoothArray = rawArray.copy()
    index = 0
    pulses = []
    pulseArea = []
    for number in smoothArray:
        #Checks if it is on the first three items in smoothArray or the last three items and will pass because the formula won't work.
        if index == 0 or index == 1 or index == 2 or index == (len(smoothArray) - 1) or index == (len(smoothArray) - 2) or index == (len(smoothArray) - 3):
            index += 1
            pass
        else:
            #Formula: (yi-3 + 2yi-2 + 3yi-1 + 3yi + 3yi+1 + 2yi+2 + yi+3) / 15
            smoothArray[index] = (smoothArray[index-3] + (2*smoothArray[index-2]) + (3*smoothArray[index-1]) + (3*smoothArray[index]) + (3*smoothArray[index+1]) + (2*smoothArray[index+2]) + smoothArray[index+3]) / 15
            index += 1

    index = 0
    findPulse = True
    for number in smoothArray:
        #Checks if there is a need to find a new pulse.
        if findPulse:
            try:
                #Checks if the voltage threshold has been met or surpassed
                if (smoothArray[index+2] - number) >= 100:
                    pulses.append(index)
                    findPulse = False
            except IndexError:
                pass
        try:
            #If data starts to decrease instead of increase, find a new pulse.
            if (smoothArray[index+3] - smoothArray[index+1]) < 0:
                findPulse = True
        except IndexError:
                pass
        index+=1
    
    for pulse in range(len(pulses)):
        area = 0
        try:
            #Adds up all of the data between the first pulse and the next pulse if next pulse comes before 50 raw data points.
            for index in range(pulses[pulse], pulses[pulse+1]):
                area = area + rawArray[index]
            pulseArea.append(area)
        #If IndexError comes up because there are no more pulses add up next 50 data points.
        except IndexError:
            for index in range(pulses[pulse], pulses[pulse] + 50):
                area = area + rawArray[index]
            pulseArea.append(area)

    fileSplit = fileName.split('.')
    fileTitle = fileSplit[0]
    #Outputs data to fileName.out
    with open(fileTitle + ".out", 'w') as outFile:
            outFile.write(f"{fileName}:\n")
            for pulse in range(len(pulses)):
                outFile.write(f"Pulse {pulse+1}: {pulses[pulse]} ({pulseArea[pulse]})\n")

    #Top subplot
    plt.subplot(2,1,1)
    plt.plot(rawArray)
    plt.ylabel('raw')

    #Bottom subplot
    plt.subplot(2,1,2)
    plt.plot(smoothArray)
    plt.ylabel('smooth')

    plt.suptitle(fileName)
    plt.savefig(f"{fileTitle}.pdf")

    #Shows graphs
    plt.show()


def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

if __name__ == "__main__":
    main()