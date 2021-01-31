class Rational:
    @staticmethod
    def gcd(a, b):
        if (b == 0):
            return a
        else:
            return Rational.gcd(b, a % b)

    def __init__(self, n=0, d=1):
        self.__g = Rational.gcd(abs(n), abs(d))
        self.numer = n//self.__g
        self.denom = d//self.__g

    def __add__(self, that):
        if (isinstance(that, int)):
            return Rational(self.numer + that*self.denom, self.denom)
        else:
            raise Exception("Sorry, number must be integer!")

    def __str__(self):
        return (str(self.numer) + "/" + str(self.denom))


x = Rational(7, 3)
y = Rational()
# z = Rational(12, 8)
print(x)
print(y)
# print(z)
print(x+1)
