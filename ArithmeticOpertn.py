
class Arithmetic():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
    def Add(self):
        self.z = self.x + self.y
        return(self.z)
    def Sub(self):
        self.z = self.x - self.y
        return(self.z)
    def Mul(self):
        self.z = self.x * self.y
        return(self.z)
    def Div(self):
        self.z = self.x / self.y
        return(self.z)
    def FDiv(self):
        self.z = self.x // self.y
        return(self.z)
    def Mod(self):
        self.z = self.x % self.y
        return(self.z)
    def Expo(self):
        self.z = self.x ** self.y
        return(self.z)

class main():
    Arithop = Arithmetic(15, 2)
    Arithop.Add()
    print(Arithop.z)

    Arithop.Sub()
    print(Arithop.z)

    Arithop.Mul()
    print(Arithop.Mul())

    Arithop.Div()
    print(Arithop.Div())

    Arithop.FDiv()
    print(Arithop.FDiv())

    Arithop.Mod()
    print(Arithop.Mod())

    Arithop.Expo()
    print(Arithop.Expo())
