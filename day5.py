# def add(): #called function
#   print("hello world")
#   n1 = int(input("enter the value of n1: "))
#   n2 = int(input("enter the value of n2: "))
#   print("Add =",n1+n2)

# add()
#how to return multiple value
# def add(): #called function

#   n1 = int(input("enter the value of n1: "))
#   n2 = int(input("enter the value of n2: "))
#   sum = n1+n2
#   mul = n1*n2
#   sub  = n1-n2
#   div = n1/n2
#   return sum,mul,sub,div

 

# result = add()
# print(result)
#tuple is immutable cannot be changed
#positional arguement
# keyword arguement
# default arguement
# variable length arguement/variable number arguement
# 1.positional arguement
# def personalInfo(fname,lname):
#   print("First Name=",fname)
#   print("Last Name=",lname)
# personalInfo("Shreeya","Bhomle")
#keyword arguement
# def personalInfo(fname, lname):
#   print("First Name= ",fname)
#   print("Last Name= ",lname)
# fname = "shreeya"
# lname = "bhomle"
# personalInfo( fname , lname)

#default arguement
# def cityName(city = "Nagpur"):
#  print(city)
# cityName("Mumbai")
# cityName("Delhi")
# cityName()
#variable length arguement
# def studentNames(*name):
#     print(name)
# studentNames("Shreeya","inaas","sayali")
# mylist = [5,2,9,7,5,6]
# #search the element 7
# def searchelement(target):
#     for i in range(len(mylist)):#mylist=6
#        print(mylist[i])#i=5,mylist[]
# searchelement(7)
# mylist = [5,2,9,7,5,6]
# #search the element 7
# def searchelement(target):
#     for i in range(len(mylist)):#mylist=6
#        if target == mylist[i]:
#            print("element found at index number ",i)
# searchelement(7)
# mylist = [5,2,9,7,5,6]
# #search the element 7
# def searchelement(target):
#     for i in range(len(mylist)):#mylist=6
#        if target == mylist[i]:
#           return i
# result = searchelement(7)
# print("element found at index number ",result)
mylist = [5,2,9,7,5,6]
#search the element 7
def searchelement(target):
    for i in range(len(mylist)):#mylist=6
       if target == mylist[i]:
          return i
    return -1
result = searchelement(10)
if result != -1:
  print("element found at index number ",result)
else:
   print("element not found")