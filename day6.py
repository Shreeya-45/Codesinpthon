# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1 #both will have same address
# fruit_list3 = fruit_list1[:] #only list3 will store list1
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#       sum += 1
#     if ls[1] == 'Kiwi':
#        sum += 20
# print(sum)
# def f(i,values = []):
#     values.append(i)
#     print(values)
# f(1)#calling function
# f(2)
# f(3)
# def func(value,values): #value = 3 , values =[1,2,3]
#     var = 1
 
#     values[0] = 44 #[44,2,3]
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])
# dict = {'c':98,'a':96,'b':97} #key value pair in dict
# for _ in sorted(dict): 
#     print(dict[_])
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1 #{'Apple':1,'Banana':2,'apple':3}
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))
# arr = [1,2,3,4]
# newarr = []
# mul1 = 1
# mul2 = 1
# mul3 = 1
# mul4 = 1
# for i in range(len(arr)):
#     if i == 0:
#          mul1 *= arr[0]*arr[1]*arr[2]*arr[3]
#          newarr.append(mul1)
         
#     if i == 1:
#         mul2 *= arr[0]*arr[2]*arr[3]
#         newarr.append(mul2)
#     if i == 2:

#         mul3 *= arr[0]*arr[1]*arr[3] 
#         newarr.append(mul3)
#     if i == 3:
#         mul4 *= arr[0]*arr[1]*arr[2]
#         newarr.append(mul4)
# print(newarr)
# input= input(str("enter string input"))
# count = 0
# char = "@","$","#","!","&","*"

# for i in range(len(input)):
#     if input[i] in char or input[i] == " ":
#          count+=1
# print(count) 
# var = 'gasgg54@#vscsd!s*'
# count = 0
# for i in var:
#      z = ord(i)
#      if z>=97 and z<=122:
#           continue
#      elif z>=48 and z<=57:
#           continue
#      else:
#          count+=1
# print(count)
# mylist1 = [1,2,3]
# mylist2 = [2,3,4]
# mylist3 = [3,4,5]
# for i in mylist1:
#     if  i in  mylist2 and i in mylist3:
#             print(i)
# arr = [0,1,0,3,1,12]
# find = 0

# for i in range(len(arr)):
#     if find in arr:
#      arr.remove(find)

#      arr.append(find)
# print(arr)
# arr = [7,3,9,2,8]
# arr.sort()
# print(arr)
# print(arr[-2])
# N = int(input())
# arr = []
# sum = 0
# for i in range(N):
#     a = int(input("enter element value"))
#     arr.append(a)
# for j in range(len(arr)):
    
#     diff = abs((arr[j]-arr[j+1]))
#     sum += diff
# print(sum)

