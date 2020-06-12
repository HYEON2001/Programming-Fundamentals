class Calculator:
    def __init__(self):
        self.list = [0,0,0,0]
    def Add(self, n1, n2):
        self.list[0] += 1
        return n1 + n2
    def Min(self, n1, n2):
        self.list[1] += 1
        return n1 - n2
    def Mul(self, n1, n2):
        self.list[2] += 1
        return n1 * n2
    def Div(self, n1, n2):
        self.list[3] += 1
        return n1 / n2
    def ShowCount(self):
        print("덧셈 : ", self.list[0])
        print("뺄셈 : ", self.list[1])
        print("곱셈 : ", self.list[2])
        print("나눗셈 : ", self.list[3])

cal = Calculator()
print("10 + 20 = {}".format(cal.Add(10,20)))
print("10 - 20 = {}".format(cal.Min(10,20)))
print("10 * 20 = {}".format(cal.Mul(10,20)))
print("10 / 20 = {}".format(cal.Div(10,20)))
print("10 * 10 = {}".format(cal.Mul(10,20)))

cal.ShowCount()