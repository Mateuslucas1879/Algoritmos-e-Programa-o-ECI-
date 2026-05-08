class C:

    x = 4

    def __init__(self,y):

        self.y = y

    def f(self,a):

        self.y += self.x * a

        self.x -= 1

        return C(self.y)

    def __repr__(self):

        return (str(self.x)+"+"+str(self.y))

print(C("b").f("a-"))