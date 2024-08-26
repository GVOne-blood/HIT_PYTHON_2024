class Tamthuc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self) -> str:
        return "{}x^2 + {}x + {}".format(self.a, self.b, self.c)
       
th1 = Tamthuc(1, 2, 3)
th2 = Tamthuc(4, 5, 6)
print(th1.__str__())
