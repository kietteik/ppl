from functools import reduce

class Element:
	pass

class Many(Element):
    def __init__(self,lst):
        self.lst = lst

class Inte(Element):
    def __init__(self,int_):
        self.int_ = int_

class Flt(Element):
    def __init__(self,flt_):
        self.flt_ = flt_

def sum(lst,func): 
    res = 0
    for x in lst:
        res += func(x)
    return res

def func(ele):
	if type(ele) is Inte:
		return 1
	elif type(ele) is Flt:
		return 0
	else:
		return sum(ele.lst,func)

print("-------------------------------------------")
print("Gian Tiep")

lst = [Inte(1),Inte(2)]
print(sum(lst,func))

lst = [Inte(1),Inte(2),Flt(3.5)]
print(sum(lst,func))

lst = [Inte(1),Inte(2),Flt(3.5),Many([Inte(1),Inte(2),Flt(3.5)])]
print(sum(lst,func))




def func1(ele):
	if type(ele) is Inte:
		return 1
	elif type(ele) is Flt:
		return 0
	else:
		return reduce(lambda x,y:x+func1(y),ele.lst,0)
print("-------------------------------------------")
print("Truc Tiep")

lst = [Inte(1),Inte(2)]
print(sum(lst,func1))

lst = [Inte(1),Inte(2),Flt(3.5)]
print(sum(lst,func1))

lst = [Inte(1),Inte(2),Flt(3.5),Many([Inte(1),Inte(2),Flt(3.5)])]
print(sum(lst,func1))