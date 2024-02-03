class Temparature():
    def __init__(self):
        pass
    
    def fahrenheit(self, tcc):
        self.tf = (self.tcc * 9/5) + 32
        return self.tf

    def celsius(self, tff):
        self.tc = (self.tff - 32) * (5/9)

        return self.tc
t = Temparature()
print(t.celsius(5))