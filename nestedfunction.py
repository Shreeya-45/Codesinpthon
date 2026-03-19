#nested function
def outerFunction():
  print("this is my outer function :")
  def innerFunction():
         print("inner Function")
  innerFunction()
outerFunction()