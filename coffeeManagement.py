import datetime
class Cafe:

    def __init__(self):
        self.name= input("Please enter your name==>");
    def greet(self):
        print(f"Hello {self.name}, Welcome to Python Cafe\n Make your day with Taste\n Python Cafe\n Remove stress \n best by TASTE")
        print("What can Python cafe serve you? Feel free to choose")
        
    def order(self):
        menu={
         "Coffee":"150",
         "Tea":"30",
         "Cake":"800",
         "Cup Cake":"35"
        }
        x=1
        price=0
        while(x==1):
            menu={
             "Coffee":"150",
             "Tea":"30",
             "Cake":"800",
             "Cup Cake":"35"
            }
            print("Coffee = 150\n Tea=30\n Cake=800\n Cup Cake=35")
            print(f"Your price till now is {price}")
    

            order1 = input("Enter your order ==>");
            if order1 in menu:
                price = price+ int(menu[order1])
                temp= input("Do you want to add more orders? Y/N==> ")
                if temp=='Y':
                    x=1;
                else:
                    x=0; 
            else:
                print(f"Sorry {self.name}, We are unable to serve you the {order1}")
        print(f"\nPython cafe is happy to serve {self.name}.\n {self.name}'s had order of Rs {price}\n ")

user = Cafe()
user.greet()
user.order()
