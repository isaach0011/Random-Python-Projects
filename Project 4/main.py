"""
Project Name: Stock Exchange Data
Author: Isaac Hill
Due Date: 10/30/2020
Course: CS1400-X04

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

This program when given a comma-separated stock value file will go through and calculate out the max the
min and the average and when it happened for each of the symbols. When reading line by line it will
check which symbol it is then see if the price is bigger or smaller than the current max or min. If it is
either, it will then set the key in that stock dictionary to be the new price. The program also sees
which is the highest or lowest price of all of the stock then sets it in a dictionary. It then outputs all
of the data to a file called "stock _summary.txt" and prints it to the console. To change the file
in which the program reads, change the value of inputFileName.
"""
def main():
    
    #Tests if file exists, if so, opens file and continues, if not, prints message and exits
    try:
        #Change file here!
        inputFileName = "stocks_data.csv"
        inputFile = open(inputFileName, 'r')
    except FileNotFoundError:
        print("file", inputFileName, "does not exist.")
        exit()
    
    outputFile = open("stock_summary.txt", 'w')
    
    # Sets up initial dictionaries and variables
    aapl = {'max':100.0, 'maxDate':'', 'min':100.0, 'minDate':'', 'sum':0, 'count':0}
    ibm = {'max':100.0, 'maxDate':'', 'min':100.0, 'minDate':'', 'sum':0, 'count':0}
    msft = {'max':100.0, 'maxDate':'', 'min':100.0, 'minDate':'', 'sum':0, 'count':0}
    recordPrice = {'maxSymbol':'', 'max':100.0, 'maxDate':'', 'minSymbol':'', 'min':100.0, 'minDate':''}
    
    #Skips the first line and begins loop for reading the input file
    inputFile.readline()
    for line in inputFile:
        lineData = line.split(',')
        
        # Sets variables to the different sections of the line
        symbol = lineData[0]
        date = lineData[1]
        price = float(lineData[2])
        
        # Checks if line is AAPL stock
        if symbol == "AAPL":
            checkStock(symbol, price, date, aapl, recordPrice)
            
        # Checks if line is IBM stock      
        if symbol == "IBM":
            checkStock(symbol, price, date, ibm, recordPrice)
            
        #Checks if line is MSFT stock
        if symbol == "MSFT":
            checkStock(symbol, price, date, msft, recordPrice)
     
    writePrintOutput(outputFile, aapl, ibm, msft, recordPrice)
    
    # Closes files
    inputFile.close()
    outputFile.close()
    
def checkStock(symbol, price, date, stock, recordPrice):
    # If stock price is bigger or smaller than in the min or max key, if so sets price to the key
    if price > stock['max']:
        stock['maxDate'] = date
        stock['max'] = price
    elif price < stock['min']:
        stock['minDate'] = date
        stock['min'] = price
                
    # Adds stock price to the sum for the symbol and ups the stock counter
    stock['sum'] += price
    stock['count'] += 1
    
    #Check if stock price is bigger or smaller than the min or max key, if so sets price to that key
    if price > recordPrice['max']:
        recordPrice['maxSymbol'] = symbol
        recordPrice['maxDate'] = date
        recordPrice['max'] = price
    elif price < recordPrice['min']:
        recordPrice['minSymbol'] = symbol
        recordPrice['minDate'] = date
        recordPrice['min'] = price
    
# Writes min, max, and average to file and prints to console
def writePrintOutput(file, aapl, ibm, msft, recordPrice):
    file.write("APPL\n" + "----\n" + "Max: %f %s\n" % (aapl['max'], aapl['maxDate']))
    file.write("Min: %f %s\n" % (aapl['min'], aapl['minDate']) +
               "Ave: %f\n\n" % (aapl['sum'] / aapl['count']))
    file.write("IBM\n" + "----\n" + "Max: %f %s\n" % (ibm['max'], ibm['maxDate']))
    file.write("Min: %f %s\n" % (ibm['min'], ibm['minDate']) +
               "Ave: %f\n\n" % (ibm['sum'] / ibm['count']))
    file.write("MSFT\n" + "----\n" + "Max: %f %s\n" % (msft['max'], msft['maxDate']))
    file.write("Min: %f %s\n" % (msft['min'], msft['minDate']) +
               "Ave: %f\n\n" % (msft['sum'] / msft['count']))
    file.write("Highest: %s %f %s\n" % (recordPrice['maxSymbol'], recordPrice['max'], recordPrice['maxDate']))
    file.write("Lowest: %s %f %s" % (recordPrice['minSymbol'], recordPrice['min'], recordPrice['minDate']))
    
    print("AAPL", "\n----", "\nMax:", aapl['max'], aapl['maxDate'],
          "\nMin:", aapl['min'], aapl['minDate'], "\nAve:", aapl['sum'] / aapl['count'])
    print("\nIBM", "\n----", "\nMax:", ibm['max'], ibm['maxDate'],
          "\nMin:", ibm['min'], ibm['minDate'], "\nAve:", ibm['sum'] / ibm['count'])
    print("\nMSFT", "\n----", "\nMax:", msft['max'], msft['maxDate'],
          "\nMin:", msft['min'], msft['minDate'], "\nAve:", msft['sum'] / msft['count'])
    print("\nHighest:", recordPrice['maxSymbol'], recordPrice['max'], recordPrice['maxDate'],
          "\nLowest:", recordPrice['minSymbol'], recordPrice['min'], recordPrice['minDate'])
    
if __name__ == "__main__":
    main()