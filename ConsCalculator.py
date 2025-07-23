class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("The Addition of a and b :",self.a+self.b)
    def sub(self):
        print("The Subraction of a and b :",self.a-self.b)
    def mul(self):
        print("The Multiplication of a and b :",self.a*self.b)
    def div(self):
        print("The Division of a and b :",self.a/self.b)
ob=calculator(int(input("Enter the first number:")),int(input("Enter the second number:")))
ob.add()
ob.sub()
ob.mul()
ob.div()
