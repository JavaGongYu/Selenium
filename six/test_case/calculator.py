class Calculator:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

