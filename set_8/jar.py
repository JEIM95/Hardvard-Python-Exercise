class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.increase = 0
        
    def __str__(self):
        cookie = ""
        if self.increase == 0:
            cookie = ""
        else:
            for i in range(self.increase):
                cookie = cookie + "🍪"
        return cookie
    
    def deposit(self, n):
        if int(n) < 0:
            raise ValueError ("Negative value")
        else:
            self.increase = self.increase + int(n)
            if self.increase > self.capacity:
                self.increase = self.increase - int(n)
                raise ValueError("Not capacity for that")
        
    def withdraw(self, n):
        if int(n) < 0:
            raise ValueError ("Negative value")
        else:
            self.increase = self.increase - int(n)
            if self.increase < 0:
                self.increase = self.increase + int(n)
                raise ValueError("Negative value. Imposible")
    
    @property
    def capacity(self):   
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Negative capacity")
        self._capacity = value
    
    @property
    def size(self):
        return self.increase
    
   