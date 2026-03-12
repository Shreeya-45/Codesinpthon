# print(2+2)
# print("2"+"2")
# val1 = int(input("enter first value:"))
# val2 = int(input("enter second value:"))
# print(val1+val2)
# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))
# print(int("4.22"))
# print(float(3))
# print(float(True))
# print(float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float(4.22))
# print(float("4"))
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# print(complex(5,-3))
# print(complex(True,False))

# print(bool())
# print(bool(0))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(1+2j))
# print(bool(0.0))
# print(bool(3.14))
# celcius to faranheit code
# centigrade = float(44)
# faranheit = (centigrade*9/5)+32
# print(faranheit)
#swap
# val1 = int(input("enter val1"))
# val2 = int(input("enter val2"))
# temp = val1
# val1 = val2
# val2 = temp 
# print(val1)
# print(val2)

# a = int(input("enter val1"))
# b = int(input("enter val2"))
# a = a+b
# b = a-b 
# a = a-b
# print(a)
# print(b)
# height = float(input("enter height in feet"))
# inch = height*12
# cm = inch*2.54
# print(inch)
# print(cm) 
# num = 1234567
# print(num)
# a = num%10 #7
# num = num // 10 #num = 123456
# b = num%10 #b=67
# num2= num // 10 #num = 12345
# c = num%10 #567
# num3 = num // 10 #num = 1234
# d = num%10 #4567
# num4 = num // 10 #num=123
# e = num%10 #34567
# num4 = num // 10 #num=12
# f = num%10 #234567
# num4 = num // 10 #num=1
# g = num%10 #1234567


# rev = a*1000000 + b*100000 + c*10000 + d
# print(rev)
# mylist = [['prashant','jha'],['85.56'],[440022,"yyy"]]
# print("example of multidimensional list: ")
# print(mylist)
# print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])
# list1 = ['prashant','jha']
# print(list1*2)
# list2 = [50,25,50]
# print(list1+list2)
# list2 = [50,25,50,'prashant']
# del list2[2]
# del list2
# print(list2)
# list2 = [50,25,50,'prashant']
# list2.clear()
# print(list2)
# name = "prashant"
# print(name)
# myname = list(name)#typecasting
# print(myname)
# for i in range(1,11):#loop will continue untill i>0
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6)
#  
#accepting days
# day = input("enter day")
# weekend = "saturday" or "sunday" or"SUNDAY" or  "SATURDAY"
# working = "monday","tuesday","wednesday","thursday","friday" 
# if day == weekend:
#     print("weekend")
# else:
#     print("working")
#wap 
# phy = int(input("marks1"))
# chem = int(input("marks2"))
# maths = int(input("marks3" ))
# total = phy + chem + maths
# percentage = (total)/3.0*100
# if percentage>=60:
#     print("eligible")
# else:
#     print("not eligible") 
    #wap accept 5 diff var and check max value print by using "simple if statement"
# a = int(input("enter a"))
# b = int(input("enter b"))
# c = int(input("enter c"))
# d = int(input("enter d"))
# e = int(input("enter e"))
# if a>b and a>c and a>d and a>e :
#     print("a is max")
# if b>a and b>c and b>d and b>e :
#     print("b is max")
# if c>a and c>b and c>d and c>e :
#     print("c is max")
# if d>a and d>b and d>c and d>e :
#     print("d is max")
# if e>a and e>b and e>c and e>d :
#     print("e is max") 
# mydict = {
#     "name":"prashant",
#     "professional": "developer",
#     "empid":1001
# }
# print(mydict)
# print(type(mydict))
# mydict = {
#     101:
#     "prashant",
#     102:"ashish",
#     "103":"mohini",
#     "104" : "trivani",
#      101: "ashish",
#      104 : "ashish"
# }
# mydict[102]="peter"
# print(mydict)
# for x in mydict:
#     print(x)
# for x in mydict.values():
#     print(x)
# for x,y in mydict.items(): #key value print
#     print(x,y)
# mydict.pop(101)
# print(mydict)
# name = "prashantjha"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[1:8:2])#increment by 2
# print(name[::-1])
# print(name[:])
# s= "prashant","ashish","sandip"
# m = "|".join(s)
# print(m)
# s= "python is high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())
# print("subject marks")
# phy = 50 
# chem = 60
# math = 70
# print("physics={} chemistry={} Math={}",format(phy,chem,math))
# print("physics={0} chemistry={1} Math={2}",format(phy,chem,math))
# print("physics={x} chemistry={y} Math={z}",format(phy,chem,math))
# total = phy+chem+math
# print("total marks",f"{total}")
# print("roll no=","7".zfill(4))
# a= 50
# b= 30
# c= 20
# d = 10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)
name = "prashant"
vow=0
con=0
for i in name:
    if (i == "a" and "e" and "i" and "o" and "u"):
        vow=vow+1
    else:
         con=con+1
print(vow)
print(con)
