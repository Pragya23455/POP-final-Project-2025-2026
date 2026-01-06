# base class
class StockItem:

    # Class variable(which is shared by all objects in base and sub classes)
    stock_category="Car accessories"
    
    # Dunder function
    def __init__(self,stock_code,quantity,price):

        #stock code should not be empty if its empty it will raise value error
        if not stock_code:
            raise ValueError("Error!! stock code cannot be empty.")
        #quantity should be in between 1 and 100 if its not in between 1 to 100 it will raise value error
        if quantity<1 or quantity>100:
            raise ValueError("Error!! Quantity must be between 1 to 100")
        #price should be greater than 0 if its not greater than 0 it will raise value error
        if price<=0:
            raise ValueError("Price must be greater than 0")
        #Price should not be empty if its empty it will raise value error
        if not price:
            raise ValueError("Error!! price cannot be empty.")
        
        self.__stock_code=stock_code
        self.__quantity=quantity
        self.__price=price
    
        # Setters 
    def setStockCode(self,stock_code):
        self.__stock_code=stock_code

    def setQuantity(self,quantity):
        self.__quantity=quantity

    def setPrice(self,price): #price without vat
        self.__price=price


    # Getters
    def getStockCode(self):
        return self.__stock_code
    
    def getQuantity(self):
        return self.__quantity
    
    def getStockName(self):
        return "Unknown Stock Name"
    
    def getStockDescription(self):
        return "Unknown Stock Description"
    
    def getPriceWithoutVAT(self):
        return self.__price
    
    def getVAT(self):
        return 17.5
    
    # calculates and return price with VAT
    def getPriceWithVAT(self):
        vat_amount=self.__price*self.getVAT()/100
        return self.__price+vat_amount

    

    # Stock Methods
    # increase stock quantity after checking the amount and ensuring it doesnot exceed 100.
    def increaseStock(self,amount):
        new_quantity= self.__quantity+amount
        
        if amount<1:
            print("Error!! Increased stock should be greater than or equal to 1.")
        elif new_quantity>100:
            print("Error!! Stock cannot be more than 100")
        else:
            self.__quantity=new_quantity
    
    
    # checks sale quantity and reduces stock if sufficient quantity is available
    def sellStock(self,amount):
        if amount<1:
            print("Error!! Sold item should not be less than 1")
        elif self.__quantity>=amount:
            self.__quantity-=amount
            return True
        else:
            return False

     # dunder function
    def __str__(self):
        return ("Stock Category:"+StockItem.stock_category
                 +"\nStock Type: "+self.getStockName()
                 +"\nDescription: "+ self.getStockDescription() 
                 +"\nStock Code : "+ str(self.getStockCode())
                 +"\nPrice without VAT: {:.2f} ".format(self.getPriceWithoutVAT())
                 +"\nPrice with VAT: {:.2f}".format(self.getPriceWithVAT())
                 +"\nTotal unit in stock:"+str(self.getQuantity()))
    
# subclass
class NavSys(StockItem):
    def __init__(self,stock_code,quantity,price,brand):
        if not brand:
            raise ValueError("Error!! Brand cannot be empty.")
        # super() is used to call methods and constructors from base class to sub class
        super().__init__(stock_code, quantity, price)
        self.__brand=brand.title() #.title() capitalizes the first letter of word
    
    # setters
    def setBrand(self,brand):
        self.__brand=brand

    # getters
    def getBrand(self):
        return self.__brand.title()
    
    # Method Overriding
    def getStockName(self):
        return "Navigation System"
    
    def getStockDescription(self):
        return "GeoVision Sat"
    
    # dunder function
    def __str__(self):
        return super().__str__()+"\nNavSys Brand:"+self.getBrand()
    
    
product=None 

while True:
    print("\n-----------------------------------------------------") 
    print("      Welcome to Car Parts and Accessories shop      ")                
    print("-----------------------------------------------------")  
    print("                1.Add new items                      ") 
    print("                2.Increase stock                     ")
    print("                3.Sell stock                         ")
    print("                4.Set New Stock Code                 ")
    print("                5.Set New price                      ")
    print("                6.Set Brand Name                     ")
    print("                7.Stock item Details                 ")
    print("                8.Exit                               ")
    print("-----------------------------------------------------") 
    
    choice=int(input("\nPlease enter your choice: "))

    if choice==1:
        try:
            # taking user input 
            stock_code=input("Enter a stock_code of your item: ")  
            quantity=int(input("Enter a quantity of your item: ") ) 
            price=float(input("Enter a price of your item: "))
            brand=input("Enter a brand: ")

            product = NavSys(stock_code,quantity,price,brand)
            print("Items added successfully \n")
        except ValueError as e:
            print(e)
        

    elif choice==2:
        if product is None:
            print("please add stock items.\n")
        else:
            increase_stock=int(input("Enter the quantity you want to increase: "))
            product.increaseStock(increase_stock)
            print("New stock is added successfully \n")

    elif choice==3:
        if product is None:
            print("please add stock items.")
        else:
            sell_stock=int(input("Enter the quantity of sold items: "))
            product.sellStock(sell_stock) 
            print("Quantity of sold items are recorded. \n")

    elif choice==4:
        if product is None:
            print("please add stock items.")
        else:
            new_stock_code=input("Enter the new stock code: ")
            product.setStockCode( new_stock_code)
            print("Stock code updated successfully. \n")

    elif choice==5:
        if product is None:
            print("please add stock items.")
        else:
            new_price=float(input("Enter the new price: "))
            product.setStockCode( new_price)
            print("Price updated successfully. \n")
    
    elif choice==6:
        if product is None:
            print("please add stock items.")
        else:
            new_brand=float(input("Enter the new brand: "))
            product.setBrand( new_brand)
            print("Brand updated successfully. \n")
        
    elif choice==7:
        if product is None:
            print("Enter the stock first.\n")
            print("No stock available \n")
        else:
            print(product)

    elif choice==8:
        print("Program exited \n")
        break

    else:
        print("Invalid enter your choice first. \n")

