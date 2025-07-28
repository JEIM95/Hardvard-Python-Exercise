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
        self.increase = self.increase + int(n)

        if self.increase > self._capacity:
            self.increase = self.increase - int(n)
            raise ValueError ("Not capacity for that")
        elif int(n) < 0:
            self.increase = self.increase + int(n)
            raise ValueError ("Negative value")
        
    def withdraw(self, n):
        self.increase = self.increase - int(n)

        if self.increase < 0:
            self.increase = self.increase + int(n)
            raise ValueError ("Not more cookies")
        elif int(n) < 0:
            self.increase = self.increase - int(n)
            raise ValueError ("Negative value")
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError ("Negative capacity")
        self._capacity = capacity
        return self._capacity
    
    @property
    def size(self):
        return self.increase
    
   