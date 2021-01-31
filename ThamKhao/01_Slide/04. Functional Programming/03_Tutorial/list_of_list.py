from functools import reduce
##def foo(a):
##	return reduce(lambda x,y: x+y,a)
##
##print(foo([[1,2,3],[4,5,6],[10,122],[1]]))
##
##
##
##convList = lambda lst: reduce(lambda x,y: x+y,lst)
##print(convList([[1,2,3],[4,5,6],[10,122],[1]]))

tinh = lambda lst: reduce(lambda x,y: y + x,lst,'c')
print(tinh(['a','b','d']))
