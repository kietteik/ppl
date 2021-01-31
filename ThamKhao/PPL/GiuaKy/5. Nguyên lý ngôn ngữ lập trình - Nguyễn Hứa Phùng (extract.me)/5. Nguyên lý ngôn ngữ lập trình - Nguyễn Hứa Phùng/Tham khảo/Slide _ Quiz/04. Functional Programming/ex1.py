def check_int(x):
    strX = str(x)
    if strX[0] == '-':
        for i in strX[1:]:
            if i != '0' and i != '1' and i != '2' and i != '3' and i != '4'and i != '5' and i != '6' and i != '7' and i != '8'and i != '9':
                return 0
    else:
        for i in strX[0:]:
            if i != '0' and i != '1' and i != '2' and i != '3' and i != '4'and i != '5' and i != '6' and i != '7' and i != '8'and i != '9':
                return 0
    return 1
def  mul_int( lst):
    lst_int = list(filter(lambda x:  check_int(x)  ,lst))
    result= 1
    print(lst_int)
    for x in lst_int:
        result = result*x
    return result
#print(mul_int([1,2,3,'a',1.5]))

def kkk(x):
    return 1111 if (x<3) else 2222 if(x>6) else 3333

def ghep_chuoi(lst,b):
    return list(map( lambda x: (x,b) , lst))
print(ghep_chuoi([1,2,3],4))

    
