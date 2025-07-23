class teacher:
    def __init__(self,name,reg_num):
        self.name=name
        self.reg_num=reg_num
    def display(self):
        print("Name :",self.name)
        print("Reg Num :",self.reg_num)
t1=teacher("John",1)
t2=teacher("Gokul",2)
t1.display()
t2.display()