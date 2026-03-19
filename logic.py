s = ""
s1 = s.replace("difficult","easy")
print(s1)
#all occurences will bee replaced
s = "abababababab"
s1 = s.replace("a","b")
print(s1)
#rstrip()==to remove spaces at right hand side
#lstrip() == to remove space at left hand side
#strip()== to remove spaces from both sides
# city = input("Enter your city Name:")
# scity = city.strip()
# if scity == 'hyderabad':
#  print("hello hydearabad....adab")
# if scity == 'chennai':
#  print("hello chennai......vanakkam")
# if scity == 'bangalore':
#  print("hello kannadiga....shubhodaya")
# else:
#   print("your entered city is invalid")

s = [i*i for i in range(1,11)]
print(s)

val = [2**i for i in range(1,6)]
print(val)
 
val2 = [i for i in s if i%2==0 ]
print(val2)
squares = {x:x*x for x in range(1,6)}
print(squares)
doubles = {x:2*x for x in range(1,6)}
print(doubles)
