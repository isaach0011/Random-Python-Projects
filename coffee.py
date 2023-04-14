"""
Program Name: coffee.py
Created by: Isaac Hill
Created on: 10/15/2021

class Coffee Machine: stores the other classes and has them interact with each other
    def oneAction(): prints information and instruction and where the user interacts with program
    def totalCash(): returns the total cash in the machine

class Selector: stores the cash box and the options for products sold
    def select(choiceIndex): handles payment for product and tells machine to make it
    
class CashBox: stores and manages the credits pending and credits recieved by machine
    def deposit(amount): takes an int and checks if its a valid input and adds it to user credits
    def returnCoins(): returns any excess credits in CashBox after purchasing a product
    def haveYou(amount): checks if there is enough credit in machine for the amount and returns True or False
    def deduct(amount): removes the price of the product from the credit put in
    def total(): returns the total cash in the machine

class Product: has information for products available from the Selector.
    def getPrice(): returns the price of the product
    def make(): prints out the process of the machine making a product

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""
class CoffeeMachine:

    def __init__(self):
        self.cashBox = CashBox()
        #Product List
        products = [Product("black", 35, ["cup","coffee","water"]),
                    Product("white", 35, ["cup","coffee","creamer","water"]),
                    Product("sweet", 35, ["cup","coffee","sugar","water"]),
                    Product("white & sweet", 35, ["cup","coffee","creamer","sugar","water"]),
                    Product("bouillon", 25, ["cup","bouillon","water"])]
        self.selector = Selector(self.cashBox, products)

    def oneAction(self):
        #Prints Menu
        print("______________________________________")
        print("    PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print("    1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon")
        print("    Sample commands : insert 25, select 1.")

        selection = input(">>> Your command: ")

        if selection == "quit":
            return False
        else:
            selection_split = selection.split(" ")
            #Checks if there are two parts to the string and if the first word is insert or select and the second part are digits.
            if len(selection_split) == 2 and (selection_split[0] == "insert" or selection_split[0] == "select") and selection_split[1].isdigit():
                if selection_split[0] == "insert":
                    self.cashBox.deposit(int(selection_split[1]))
                if selection_split[0] == "select":
                    #Checks if select comes back as True. Showing the user has money and the product was made.
                    if(self.selector.select(int(selection_split[1]) - 1) == True):
                        self.cashBox.returnCoins()
                return True
            #Checks if there is only one part to the string and it says only cancel.
            elif len(selection_split) == 1 and selection_split[0] == "cancel":
                self.cashBox.returnCoins()
                return True
            else: 
                print("Invalid Command.") 
                return True 

    def totalCash(self):
        #Returns total amount in the cashBox
        return self.cashBox.total()
        
class Selector:
    def __init__(self, cashBox, products): 
        self.cashBox = cashBox
        self.products = products
        
    def select(self, choiceIndex):  
        #Gets price of item selected
        price = self.products[choiceIndex].getPrice() 
        #Checks if credit is greater than or equal to the price.
        if self.cashBox.credit >= price: 
            #Makes and deducts credits
            self.products[choiceIndex].make() 
            self.cashBox.deduct(price) 
            return True 
        #If not enough money print an error message
        else: 
            print("Sorry, Not enough money deposited") 
            return False 

class CashBox:
    def __init__(self): 
        self.credit = 0 
        self.totalReceived = 0
        
    def deposit(self, amount):
        #Checks if number passed is a valid coin value and adds that to credit
        if amount == 5 or amount == 10 or amount == 25 or amount == 50: 
            self.credit = self.credit + amount 
            print("Depositing "+ str(amount) +" cents. You have "+ str(self.credit) +" cents credit.")
        #Print error if invalid
        else: 
            print("INVALID AMOUNT >>>") 
            print("We only take half-dollars, quaters, dimes, and nickels.") 

    def returnCoins(self):
        #Checks if the current credits aren't zero and print a message saying returning extra credits and set the credits to zero 
        if not self.credit==0: 
            print("Returning " + str(self.credit) + " cents.") 
            self.credit=0
            
    def haveYou(self, amount):
        #Checks if you have enough credits to purchase item.
        if(amount <= self.credit):
             return True
        else:
            return False
    
    def deduct(self, amount):
        #Deduct how ever much funds are passed to the function from credits and add it to totalRecieved
        self.totalReceived = self.totalReceived + amount
        self.credit = self.credit - amount
    
    def total(self):
        #Return totalReceived
        return self.totalReceived

class Product:
    def __init__(self, name, price, recipe):
        self.name = name 
        self.price = price
        self.recipe = recipe 
        
    def getPrice(self):
        #Returns price of item
        return self.price
    
    def make(self):
        print(f"Making {self.name}:") 
        #Prints out the ingredients for each item in recipe list
        for ingredient in self.recipe: 
            print(f"\tDispensing {ingredient}")
            
def main(): 
    m = CoffeeMachine() 
    #loops for as long as oneAction() returns true.
    while m.oneAction(): 
        pass 
    #Prints total cash made from machine
    total = m.totalCash() 
    print(f"Total cash: ${total/100:.2f}") 

if __name__ == "__main__":
    main()