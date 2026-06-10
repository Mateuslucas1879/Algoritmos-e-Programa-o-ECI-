class arvbin:
    def __init__(self, node = None):
        self.node = node
        
    def insert(self,key,value):
        if self.node == None:
            self.node = no(key,value,arvbin(None),arvbin(None))
        elif self.node.key > key: self.node.left.insert(key,value)
        elif self.node.key < key: self.node.right.insert(key,value)
        else: raise ValueError
            
    def delete(self,key):
        if self.node == None: raise ValueError
        elif self.node.key > key: self.node.left.delete(key)
        elif self.node.key < key: self.node.right.delete(key)
        else: 
            if self.node.left.node == None:
                self.node = self.node.right.node
            elif self.node.right.node == None:
                self.node = self.node.left.node
            else: # tem os filhos!
                sv,sk = self.node.right._proximo()
                self.node.key = sk
                self.node.valor = sv
                self.node.right.delete(sk)
        
    def _proximo(self):
        if self.node.left.node == None:
            return (self.node.valor,self.node.key)
        else:
            return self.node.left._proximo()
        
    def find(self,key):
        if self.node == None: raise IndexError
        elif self.node.key > key: return self.node.left.find(key)
        elif self.node.key < key: return self.node.right.find(key)
        else: return self.node.valor
        
    def __repr__(self):
        s = '['
        if self.node != None:
            s += self.node.left.__repr__()+','+str(self.node.key)+','+self.node.right.__repr__()
        s +=']'
        return s

class no:
    def __init__(self, key, valor, left=None, right=None):
        self.key,self.valor, self.left, self.right = key,valor, left, right
    
    def __repr__(self):
        s = '(' + str(self.key) + ',' + str(self.valor) + ')'
        return s
     
t = arvbin()
for x in [26,15,12,19,100,45,135]: t.insert(x,'teste'+str(x))
print(t)
t.delete(19)
t.delete(26)
print(t)
print(t.find(100))
print(t.node.right.node.right.node)

