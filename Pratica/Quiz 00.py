class C:

    a = 1

    def __init__(self,x=[]):

        self.x = x

    def g(self,a):

        self.x += [a]

        self.a += 1

        return C(self.x)

    def __repr__(self):

        return (str(self.x*self.a))

obj = C().g(1)

obj.g(3)

C.a = 2

print(obj.g(2))