class CoffeeMachine: 
    def __init__(self): 
        self.cashBox = CashBox() 
        self.selector = Selector()
        self.totalMoney=0
        self.coffee=[]

        self.coffee.append(Product("black",35,["cup","coffee","water"])) 
        self.coffee.append(Product("white",35,["cup","coffee","creamer","water"])) 
        self.coffee.append(Product("sweet",35,["cup","coffee","sugar","water"])) 
        self.coffee.append(Product("white and sweet",35,["cup","coffee","creamer","sugar","water"])) 
        self.coffee.append(Product("bouillon",25,["cup","bouillon","water"])) 

    def oneAction(self): 
        print("______________________________________") 
        print("    PRODUCT LIST: All 35 cents, except bouillon (25 cents)") 
        print("    1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon") 
        print("    Sample commands : insert 25, select 1.") 
        command=input(">>> Your command: ") 
        if command=="quit": 
            return False 
        else: 
            splitStr=command.split(" ") 
            if len(splitStr)==2 and (splitStr[0]=="select" or splitStr[0]=="insert") and splitStr[1].isnumeric(): 
                if splitStr[0]=="insert": 
                    self.cashBox.deposit(int(splitStr[1])) 
                if splitStr[0]=="select": 
                    if(self.selector.select(self.coffee[int(splitStr[1])-1])==True): 
                        self.cashBox.returnCoins() 
                        price=self.coffee[int(splitStr[1])-1].getPrice() 
                        self.totalMoney=self.totalMoney + price
                return True
            elif len(splitStr)==1 and splitStr[0]=="cancel": 
                self.cashBox.returnCoins() 
            else: 
                print("Invalid Command") 
                return True 

    def totalCash(self): 
        return self.totalMoney 
    
class CashBox: 
    def __init__(self): 
        self.credit = 0 
        self.totalReceived = 0
        
    def deposit(self, amount): 
        if amount == 5 or amount == 10 or amount == 25 or amount == 50: 
            self.credit = self.credit + amount 
            print("Depositing "+ str(amount)+" cents. You have "+str(self.total())+" cents credits")
        else: 
            print("INVALID AMOUNT >>>") 
            print("We take only half-dollars, quaters, dimes, and nickels.") 

    def returnCoins(self): 
        if not self.credit==0: 
            print("Returning "+str(self.credit)+" cents") 
            self.credit=0
            return self.credit 
            
    def haveYou(self,amount): 
        if(amount<=self.credit):
             return True 
    
    def deduct(self,amount): 
        self.credit=self.credit-amount 
    
    def total(self): 
        return self.credit 
        
class Selector: 
    #def __init__(self,cashBox): 
    #    self.cashBox=cashBox 
    def __init__(self): 
        self.cashBox = CashBox()
        self.products = []
        
    def select(self,product): 
        price=product.getPrice() 
        print(price)
        print(self.cashBox.total())
        if self.cashBox.total()>=price: 
            product.make() 
            self.cashBox.deduct(price) 
            return True 
        else: 
            print("Sorry, Not enought money deposited") 
            return False 
            
class Product: 
    def __init__(self,name,price,recipe): 
        self.name=name 
        self.price=price 
        self.recipe=recipe 
        
    def getPrice(self): 
        return self.price 
    
    def make(self): 
        print(f"Making {self.name}:") 
        for ingredient in self.recipe: 
            print(f"\tDispensing {ingredient}")
            
def main(): 
    m=CoffeeMachine() 
    while m.oneAction(): 
        pass 
    total=m.totalCash() 
    print(f"Total cash: ${total/100:.2f}") 
        
main() 