# for i,j in zip(range(1,6), range(5,0,-1)):
#  if i == 3 and j == 3:
#   continue
# print(i," ",j)
# i=1
# while i<=5:
#     print(i)
#     i = i+1
# username =" "
# password =" "
# while username != "admin" and password != "hello":
#       username  = input ("Enter user name : ")
#       password  = input ("Enter password : ")
#sum of n numbers
# n = int(input("enter number"))
# sum = 0
# i = 1
# while i<=n:
#     sum = sum + i 
#     i=i+1
# print("the sum of first",n,"numbers is:",sum)
# name = "prashant"
# newname = " "
# for i in name:
#    if i not in newname:
#          newname += i
# print(name)
# print(newname)

# print(name[::-1])
# mycart = [10,20,200,300,800,60,70]
# for i in mycart:
#     if i>400:
#         print("this is my purchased cart item")
#         continue
#     print(i)
# name = "racecar"
# name = input("enter string:")
# if name == name[::-1]:
#     print("its a palindrone")
# else:
#     print("not a palindrone")
# name1 = "listen"
# name2 = "silent"
# sum=0
# sum1=0
# for i in name1:
#     sum=sum+1
# for i in name2:
#     sum1=sum1+1
# if sum==sum1:
#     print("it is anagram")
# mydict = {
#     101:"prashant",
#     102:"ashish",
#     "103":"mohini",
#     "104" : "trivani",
#      101: "ashish",
#      104 : "ashish"
#   }
# del(mydict)
# print(mydict)
# for i in range(1,4): #outer loop=rows
#     for j in range(1,4): #inner loop = columns
#         print(i,end=" ")
#     print()
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ") 
#     print()
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()