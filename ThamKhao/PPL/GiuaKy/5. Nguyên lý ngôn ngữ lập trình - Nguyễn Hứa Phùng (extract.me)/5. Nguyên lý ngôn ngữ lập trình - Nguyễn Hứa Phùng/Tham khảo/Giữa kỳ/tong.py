from functools import reduce

def sumlst(lst):
    sum = lambda sublst:reduce(lambda x,y: x+y,sublst,0)
    index_lst = [x for x in range(1,len(lst)+1)]
    return list(map(lambda x: sum(lst[0:x]) , index_lst))
print(sumlst([1,2,3,4,5]))
