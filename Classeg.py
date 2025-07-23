class student:
    def __init__(self):
        self.name=""
        self.reg_num=""
    def display(self):
        print("Name :",self.name)
        print("Reg Num :",self.reg_num)
ob=student()
ob2=student()
ob.name="Arun"
ob.reg_num="5"
ob2.name="Ram"
ob2.reg_num="7"
ob.display()
ob2.display()