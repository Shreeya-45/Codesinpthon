#wap to perform arithmatic operation using functional programming approach
#functions help to achieve modularity approach
import sys #it stops the function all infinite times repetition
def addition(num1,num2):
    print("Addition",num1+num2)
     # called functions
    #it skips body we cannot keep function empty so we use pass
def substraction(num1,num2): # called functions
    #it skips body we cannot keep function empty so we use pass
      print("Addition",num1-num2)
      sub = val1-val2 
def Multiplication(num1,num2):
      # called functions
    #it skips body we cannot keep function empty so we use pass
    print("multiplication",num1*num2)
def division(num1,num2):# called functions
     print("division",num1/num2)#it skips body we cannot keep function empty so we use pass
while True:
       print("1.Addition")
       print("2.subtraction")
       print("3.Multiplication")
       print("4.division")
       print("5. Exit")
       choice = int(input("enter your choice from above options :"))
       if choice == 5:
           sys.exit()
       val1 = int(input("enter first value"))
       val2 = int(input("enter second value"))
       if choice == 1:
            addition(val1,val2)#call addition function
       elif choice == 2:
            substraction(val1,val2)
       elif choice == 3:
            Multiplication(val1,val2)
       elif   choice == 3:
            division(val1,val2)
       else:
          print("you have entered wrong choice")
          
        

        
        