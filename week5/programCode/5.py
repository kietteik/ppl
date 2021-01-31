def flatten(lst):
    return [] if not lst else lst[0]+flatten(lst[1:])


print(flatten([[1, 2], [3], [4, 5, 6, 7], [8]]))
print(flatten([]))
