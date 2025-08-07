class dad():
    def phone(self):
        print("Dad's Phone")
class mom():
    def sweet(self):
        print("Mom's Sweet")
class son(dad,mom):
    def laptop(self):
        print("Son's Laptop")
ram=son()
ram.phone()
ram.sweet()
