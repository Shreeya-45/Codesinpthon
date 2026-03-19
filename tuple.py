init_tuple = ()
print(init_tuple.__len__())

init_tuple_a= 'a','b'
init_tuple_b = ('a','b')#in tuple circle bracket is not mandatory
print(init_tuple_a == init_tuple_b)
 

init_tuple_a= '1' ,'2'
init_tuple_b= ('3','4')
print(init_tuple_a + init_tuple_b)

l = [1,2,3]
init_tuple = ('Python',)*(l.__len__() - l[::-1][0])#if , then tuple
print(init_tuple)

init_tuple = ('python')*3
print(type(init_tuple))#if , not present string

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)#'tuple'object does not support item assignment,tuple is immutable non changable

init_tuple = ((1,2),)*7
print(len(init_tuple[3:8]))
