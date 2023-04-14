"""
Project Name: Was Clinton Right?
Author: Isaac Hill
Due Date: 12/18/2020
Course: CS1400-X04

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

To run this program all that needs to be done is press run. The program will look at files BLS_private.csv
and Presidents.txt and create lists and a dictionary containing this data. It will then go through totaling
out the jobs created during each person's presidency. It will then output that data and show the total
amount of jobs created by the each party and both parties. One of the biggest things that I struggled with
and learned was figuring out to either use a list or a dictionary. I don't think I got the most effiecient storage
for this data but it still seems to work well. I think the numbers may be off just a bit too with some rounding
going on but it does come close enough that it makes Clinton still correct.
"""
def main():
    #Opens files
    presidentialDataFile = open('presidents.txt','r')
    jobDataFile = open('BLS_private.csv','r')
    
    presidents,parties = getPresidentData(presidentialDataFile)
    jobData = getJobData(jobDataFile)
    totals = getTotals(jobData,presidents)
    
    repTotal = 0
    demTotal = 0
    
    #Prints output and totals for Republicans
    print("Republicans:")
    for presidentTotals in totals:
        if parties[presidentTotals[0]] == "Republican":
            repTotal += presidentTotals[1]
            print(presidentTotals[0], ":", round(presidentTotals[1]/1000,2), "million jobs created")
    print("\nTotal jobs created by republicans:", round(repTotal/1000,2), "million jobs\n")
    
    #Prints output and totals for Democrats
    print("Democrats:")
    for presidentTotals in totals:
        if parties[presidentTotals[0]] == "Democrat":
            demTotal += presidentTotals[1]
            print(presidentTotals[0], ":", round(presidentTotals[1]/1000,2), "million jobs created")
    print("\nTotal jobs created by democrats:", round(demTotal/1000,2), "million jobs\n")
    
    print("Total jobs created:", round((demTotal + repTotal)/1000,2), "million jobs\n")

    print("While the numbers that Clinton said are not exact, 24 million for republicans and")
    print("42 million for democrats, the numbers are still close.")
    print("This makes Clinton's point still correct, making him right.")
    #closes files
    presidentialDataFile.close()
    jobDataFile.close()
    
#Returns a list of lists that includes the data from each line skipping the table info at the top.
def getJobData(file):
    jobData = []
    row = 1
    for line in file:
        if row > 13:
            fileData = line.split(',')
            jobData.append(fileData)
        row += 1
    return jobData
'''
Returns two dictionaries one has the presidents and the parties they are in 
and the other the years and which person was president that year
'''
def getPresidentData(File):
    president = {}
    parties = {}
    for line in File:
        presidentData = line.split(',')
        parties[presidentData[0]] = presidentData[1]
        for i in range(2, len(presidentData)):
            president[int(presidentData[i])] = presidentData[0]
    return president,parties

#Returns a list of lists that contain the presidents and the total amount of jobs they created
def getTotals(data,presidents):
    totals = []
    bigData = {}
    #Creates keys in the dictionary that have the presidents names
    for i in presidents:
        president = presidents[i]
        bigData[president] = []
    #Adds values that are lists to dictionary that contain job data
    for annualJobData in data:
        annualJobData[0] = int(annualJobData[0])
        bigData[presidents[annualJobData[0]]].extend(annualJobData[1:])
    #Creates new list that contains the total jobs created by each president 
    for i in bigData:
        jobs = bigData[i]
        presidentJobsCreated = [i]
        total = int(jobs[-1]) - int(jobs[0])
        presidentJobsCreated.append(total)
        totals.append(presidentJobsCreated)
    return totals
 
if __name__ == "__main__":
    main()