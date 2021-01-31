from functools import reduce
"""def foo(a):
	return reduce(lambda x,y: x+y,a)

print(foo([[1,2,3],[4,5,6],[10,122],[x]]))"""

lst = [0,1,2,3,4,5]
str_lst = reduce(lambda x,y:x+str(y),lst,'')
print(str_lst)



a = "k"
b = a.join("h")
print(b)