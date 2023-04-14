"""
Program Name: coffee.py
Created by: Isaac Hill
Last Modified Date: 2/26/21

Description:

class Coffee Machine: stores the other classes and has them interact with each other
    def oneAction(): prints information and instruction and where the user interacts with program
    def totalCash(): returns the total cash in the machine

class Selector: stores the cash box and the options for products sold
    def select(choiceIndex): handles payment for product and tells machine to make it
    
class CashBox:
    def deposit(amount): 
        def returnCoins(): returns any excess credits in CashBox after purchasing a product
        def haveYou(amount): checks if there is enough credit in machine for the amount and returns True or False
        def deduct(amount): removes the price of the product from the credit put in
        def total(): returns the total cash in the machine

class Product:
    def getPrice(): returns the price of the product
    def make(): prints out the process of the machine making a product

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""
class CoffeeMachine:
    """
    CoffeeMachine class: Contains the other classes and has them interact with each other

    Class attributes:
        cashBox: Creates a CashBox object
        selector: Creates a Selector object passing the cashbox created by CoffeeMachine and passes products
    """
    def __init__(self):
        self.cashBox = CashBox()
        products = [Product("black", 35, ["cup","coffee","water"]),
                    Product("white", 35, ["cup","coffee","creamer","water"]),
                    Product("sweet", 35, ["cup","coffee","sugar","water"]),
                    Product("white & sweet", 35, ["cup","coffee","creamer","sugar","water"]),
                    Product("bouillon", 25, ["cup","bouillon","water"])]
        self.selector = Selector(self.cashBox, products)

    def oneAction(self):
        """    
        This function prints information and instruction and asks the user to make a selection and will then 
        based on the selection put money in, select a product to make, or exit the program.
    
        Function parameters:           
            None

        Return values:        
            Boolean: This will stop the loop in main() so the program exits.
        """
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
        """    
        Returns the total cash in the machine from the cashBox.
    
        Function parameters:  
            None
        Return values:        
            self.cashBox.total() (int): total cash in the machine from totalReceived.
        """
        return self.cashBox.total()
        
class Selector:
    """
    Selector class: stores the cash box and the options for products sold

    Class attributes:
        cashBox: accesses cashBox made in CoffeeMachine
        products: a list of products sold and information about them.
    """
    def __init__(self, cashBox, products): 
        self.cashBox = cashBox
        self.products = products
        
    def select(self, choiceIndex):
        """    
        Function description    
    
        Function parameters:        
            ChoiceIndex (int):
         
        Return values:        
            Boolean: returns if there is enough credit for selected product.   
        """
        price = self.products[choiceIndex].getPrice() 
        if self.cashBox.credit >= price: 
            self.products[choiceIndex].make() 
            self.cashBox.deduct(price) 
            return True 
        else: 
            print("Sorry, Not enough money deposited") 
            return False 

class CashBox:
    """
    CoffeeMachine class:

    Class attributes:
        cashBox:
        selector:
    """
    def __init__(self): 
        self.credit = 0 
        self.totalReceived = 0
        
    def deposit(self, amount):
        """    
        Function description    
    
        Function parameters:        
            x: current x location on drawing grid        
         
        Return values:        
            None   
        """
        if amount == 5 or amount == 10 or amount == 25 or amount == 50: 
            self.credit = self.credit + amount 
            print("Depositing "+ str(amount) +" cents. You have "+ str(self.credit) +" cents credit.")
        else: 
            print("INVALID AMOUNT >>>") 
            print("We only take half-dollars, quaters, dimes, and nickels.") 

    def returnCoins(self):
        """    
        Function description    
    
        Function parameters:           
         
        Return values:        
            None   
        """
        if not self.credit==0: 
            print("Returning " + str(self.credit) + " cents.") 
            self.credit=0
            
    def haveYou(self, amount):
        """    
        Function description    
    
        Function parameters:        
            x: current x location on drawing grid          
         
        Return values:        
            None   
        """
        if(amount <= self.credit):
             return True
        else:
            return False
    
    def deduct(self, amount):
        """    
        Function description    
    
        Function parameters:        
            x: current x location on drawing grid        
         
        Return values:        
            None   
        """
        self.totalReceived = self.totalReceived + amount
        self.credit = self.credit - amount
    
    def total(self):
        """    
        Function description    
    
        Function parameters:        
         
        Return values:        
            None   
        """
        return self.totalReceived

class Product:
    """
    Product class: Has information for products available from the Selector.

    Class attributes:
        name: the name of the product.
        price: the price the product costs.
        recipe: a list of ingredients needed to make the product.
    """
    def __init__(self, name, price, recipe): 
        self.name=name 
        self.price=price 
        self.recipe=recipe 
        
    def getPrice(self):
        """    
        Function description    
    
        Function parameters:          
         
        Return values:        
            None   
        """
        return self.price 
    
    def make(self):
        """    
        Function description    
    
        Function parameters:         
         
        Return values:        
            None   
        """
        print(f"Making {self.name}:") 
        for ingredient in self.recipe: 
            print(f"\tDispensing {ingredient}")
            
def main(): 
    m = CoffeeMachine() 
    while m.oneAction(): 
        pass 
    total = m.totalCash() 
    print(f"Total cash: ${total/100:.2f}") 

if __name__ == "__main__":
    main()