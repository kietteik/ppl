def dist(lst, n):
    return [] if not lst else [(lst[0], n)]+dist(lst[1:], n)


print(dist([1, 2, 3], 4))
