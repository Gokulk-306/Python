class grandpa():
    def phone(self):
        print("Grandpa Phone")
class dad(grandpa):
    def money(self):
        print("Dad's Money")
class son(dad):
    def laptop(self):
        print("Son's Laptop")
ram=son()
ram.phone()
ram.money()
