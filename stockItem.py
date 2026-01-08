# --------------------------------BASE CLASS--------------------------------
class StockItem:

    # Class variable(which is shared by all objects in base and sub classes)
    stock_category="Car accessories"
    
    def __init__(self,stock_code,quantity,price):
        #empty list of errors which collects all errors
        errors =[] 
        if not stock_code:
            errors.append("Error!! stock code cannot be empty.")
        if quantity<1 or quantity>100:
            errors.append("Error!! Quantity must be between 1 to 100")
        if price<=0:
            errors.append("Price must be greater than 0")
       

        # if any errors exists,raise them together
        # "\n".join(errors) combines all error messages line by line
        if errors:
            raise ValueError("\n".join(errors))
        
        self.__stock_code=stock_code
        self.__quantity=quantity
        self.__price=price
        

        # Setters 
    def setStockCode(self,stock_code):
        if not stock_code:
            raise ValueError("Error!! stock code cannot be empty.")
        self.__stock_code=stock_code

    def setQuantity(self,quantity):
        if quantity<1 or quantity>100:
            raise ValueError("Error!! Quantity must be between 1 to 100")
        self.__quantity=quantity

    def setPrice(self,price): #price without vat
        if price<=0:
            raise ValueError("Price must be greater than 0")
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
            return False
        elif new_quantity>100:
            print("Error!! Stock cannot be more than 100")
            return False
        else:
            self.__quantity=new_quantity
            return True
    
    
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
     
# ------------------------------------SUB CLASS-----------------------------------------------
class NavSys(StockItem):
    def __init__(self,stock_code,quantity,price,brand):
        if not brand:
            raise ValueError("Error!! Brand cannot be empty.")
        # super() is used to call methods and constructors from base class to sub class
        super().__init__(stock_code, quantity, price)
        self.__brand=brand.title() #.title() capitalizes the first letter of word
    
    # setters
    def setBrand(self,brand):
        if not brand:
            raise ValueError("Error!! Brand cannot be empty.")
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
    
   
#----------------------------lOGIN---------------------------------------------
def login():
    print("\n -------Login-------")  
    username=input("Username: ")
    password=input("Password: ")

    if not username or not password:
        print("username or password cannot be empty")
        return False
    try:
        f= open("users.txt","r")
        # reads each user record from file
        for line in f:
        # splits the recorded username and password and if it input match it successfully login
            u,p=line.strip().split(",")
            if username==u and password==p:
                print("Login Successful")
                return True
       
        print("Invalid username or password")
        f.close()
        return False

    except FileNotFoundError:
        print("Error!! Users file not found.")
        return False

# -------------------------------ADD NEW USERS(WORKERS)-----------------------------
def add_users():
    print("\n -------ADD NEW USERS-------")  
    username=input("Username: ")
    password=input("Password: ")
       
    if not username or not password:
            print("username or password should not be empty")
            return False
        
    try:
        f= open("users.txt","r")
        for line in f:
            # takes the first item(username) and compares it with the username that user enters.
            # if matches,the user already exists in file
            if line.split(",")[0]==username:
                print("User already exists")
                return True
    except FileNotFoundError:
        pass

    f= open("users.txt","a")
    f.write(f"{username},{password}\n")
    f.close()

    print("User added successfully")

# --------------------------------Users Menu------------------------------------------
def users_menu(): 
    logged_in = False               
    while not logged_in:
        print("\n1. Login")
        print("2. Add New User")

        try:
            ch = int(input("Choose option: "))

            if ch == 1:
                logged_in=login()
            elif ch == 2:
                add_users()
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a number 1 or 2")
    return logged_in
    


# ---------------------------------------------Main Menu---------------------------------------------
def menu():
    
        logged_in=users_menu()
        product=None 
        while logged_in:
            print("\n-----------------------------------------------------") 
            print("      Welcome to Car Parts and Accessories shop      ")                
            print("-----------------------------------------------------")  
            print("                1.Add new items                      ") 
            print("                2.Increase stock                     ")
            print("                3.Sell stock                         ")
            print("                4.Set New Stock Code                 ")
            print("                5.Set New price                      ")
            print("                6.Set Brand                          ")
            print("                7.Stock item Details                 ")
            print("                8.Logout                             ")
            print("-----------------------------------------------------") 
            try:    
                choice=int(input("Please enter your choice: "))

                if choice==1:
                    try:
                    # taking user input 
                        stock_code=input("Enter a stock_code of your item: ")  
                        quantity=int(input("Enter a quantity of your item: ") ) 
                        price=float(input("Enter a price of your item: "))
                        brand=input("Enter a brand:")
                        product = NavSys(stock_code,quantity,price,brand)
                        print("Items added successfully \n")
                    except ValueError as e:
                        print(e)
                        

                elif choice==2:
                        if product is None:
                            print("please add stock items.\n")
                        else:
                            increase_stock=int(input("Enter the quantity you want to increase: "))
                            increaseStock=product.increaseStock(increase_stock)
                            if increaseStock:
                                print("New stock is added successfully \n")

                elif choice==3:
                        if product is None:
                            print("please add stock items.")
                        else:
                            sell_stock=int(input("Enter the quantity of sold items: "))
                            sellStock=product.sellStock(sell_stock)
                            if sellStock: 
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
                            product.setPrice( new_price)
                            print("Price updated successfully. \n")
                
                elif choice==6:
                        if product is None:
                            print("please add stock items.")
                        else:
                            brand=input("Enter the new brand: ")
                            product.setBrand(brand)
                            print("Price updated successfully. \n")
                            
                elif choice==7:
                    
                        if product is None:
                            print("Enter the stock first.\n")
                            print("No stock available \n")
                        else:
                            print(product)



                elif choice==8:
                    print("Logged out successfully \n")
                    logged_in=False
                    break
                else:
                    print("Invalid choose from the given option 1-7. \n")
                    
            except ValueError as e:
                print (f"Error was {e}")
            except Exception as e:
                print (f"Error was {e}")

menu()
