class Exp:
    def __init__(self, exp):
        self.exp = exp
    def eval(self):
        return Number(eval(self.exp))

class Number:
    def __init__(self, num):
        self.num = num
    def print(self):
        print(self.num)

if __name__ == '__main__':
    exp = input('Moi nhap bieu thuc can tinh: ')
    x = int(input('Moi nhap x: '))
    t = Exp(exp)
    t.eval().print()