class lista_enc:
    def __init__(self, node = None):
        self.__value = node
        self.__next = None
    def empty(self):
        return self.__value == None and self.__next == None
    def add(self,x):
        new = lista_enc(self.__value)
        self.__value = x
        new.__next = self.__next
        self.__next = new
    def remove(self):
        if self.__next == None:
            self.__value == None
        else:
            self.__value = self.__next.__value
            self.__next = self.__next.__next
    def value(self):
        return self.__value
    def next(self):
        return self.__next
    def __repr__(self):
        l = self
        if self.empty():
            return "->"
        s = ""
        while not l.empty():
            s += "->["+str(l.value())+"]"
            if l.next() == None:
                break
            l = l.next()
        return s
    def __len__(self):
        if self.empty(): return 0
        i = 1
        l = self.next()
        while not l.empty():
            i += 1
            l = l.next()
        return i
    def __getitem__(self,i):
        if type(i) != int:
            raise TypeError
        if i < 0: raise IndexError
        if self.empty(): raise IndexError
        it = 0
        l = self
        while it < i:
            if l.__next == None:
                raise IndexError
            l=l.next()
            it += 1
        return l.value()
    def __setitem__(self,i,x):
        if type(i) != int:
            raise TypeError
        if i < 0: raise IndexError
        it = 0
        l = self
        while it < i:
            if l.__next == None:
                l.__next = lista_enc()
            l=l.next()
            it += 1
        l.__value = x
    def __iter__(self):
        l = self
        while not l.empty():
            yield l.value()
            if l.next() == None:
                break
            l = l.next()
    def __contains__(self, item):
        l = self
        while not l.empty():
            if l.value() == item: return True
            if l.next() == None:
                break
            l = l.next()
        return False
    def __add__(self, other):
        prim = n = lista_enc()
        l = self
        while not l.empty():
            n.__value = l.__value
            n.__next = lista_enc()
            n = n.next()
            if l.next() == None:
                break
            l = l.next()
        l = other
        while not l.empty():
            n.__value = l.__value
            if l.next() == None:
                n.__next = None
                break
            n.__next = lista_enc()
            l = l.next()
            n = n.next()
        return prim
        
       
      
   
x = lista_enc()
print(x,len(x))
x.add(100)
x.add("luidi")
x.add([1])
x.add(-100)
print(x,len(x))
x.next().remove()
print(x,len(x))
print(x.next(),len(x.next()) )

print(x[0],x[2])
x[0] = "que doido"
x[10] = "ahh??"
print(x)
print(100 in x,321 in x)

for i in x:
    print(i)
y = x+x
print(x)
print(y)