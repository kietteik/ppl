def adouble(lst):
    return [x*2 for x in lst]


def bdouble(lst):
    if len(lst) == 1:
        return [lst[0]*2]
    else:
        return [lst[0]*2]+bdouble(lst[1:])


def cdouble(lst):
    return list(map(lambda x: x*2, lst))


print(adouble([5, 7, 12, -4]))
print(bdouble([5, 7, 12, -4]))
print(cdouble([5, 7, 12, -4]))
