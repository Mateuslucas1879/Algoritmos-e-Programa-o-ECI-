class D:

    def __init__(self,a,b):

        self.d = {}

        for x,y in zip(a,b):

            self.d[x] = self.d.get(x,set())

            self.d[x].add( y )

    def g(self,l):

        return [len (self.d.get(a,set())) for a in l]

print (D("aaaabbccc","xxxyyyzz").g("abc"))

print (D("abcdabcd",range(10)).g(["a","b",0,1]))
