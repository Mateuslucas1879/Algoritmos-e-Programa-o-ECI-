class heap:
    def __init__(self,A):
        self.A = A[:]
        self.size = len(A)
        self.buildheap()
        
    def pai(self,i):
        return (i+1)//2-1
    
    def left(self,i):
        return 2*i+1
    
    def right(self,i):
        return 2*(i+1)
    
    def heapify(self,i):
        l,r = self.left(i),self.right(i)
        if l < self.size and self.A[l] > self.A[i]: m = l
        else: m = i
        if r < self.size and self.A[r] > self.A[m]: m = r
        if m != i:
            self.A[i],self.A[m] = self.A[m],self.A[i]
            self.heapify(m)
            
    def buildheap(self):
        for i in range((self.size//2),-1,-1):
            #print(i,self.A[i],self.A,end=' ')
            self.heapify(i)
            #print(self.A)
    
    def heapsort(self):
        for i in range(self.size-1,0,-1):
            self.A[0],self.A[i] = self.A[i],self.A[0]
            self.size -= 1
            self.heapify(0)
        b = self.A[:]
        self.size = len(self.A)
        self.buildheap()
        return b
    
    def max(self):
        return self.A[0]
    
    def extract_max(self):
        pass
    
    def increase_key(self,i,key):
        pass
    
    def insert(self, key):
        pass
    
    def __repr__(self):
        return str(self.A)
    
A = [5,2,4,6,1,3]

h = heap(A)
print(h)
B = h.heapsort()
print(B)