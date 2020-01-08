class Myclass: # 定义类
    def __init__(self,x,y): # 定义初始化方法
        self.x = int(x)
        self.y = int(y)
    def add(self): # 定义方法
        return self.x + self.y * self.x

class sheclass(Myclass):
    def sub(self,a,b):
        return  a-b*a

print(sheclass(4,3).add()) # 调用类方法