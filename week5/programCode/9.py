def powGen(n):
    def inside(x):
        return x**n
    return inside


print(powGen(2))
square = powGen(2)
print(square(4))
