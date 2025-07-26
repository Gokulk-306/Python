class phone():
    chargertype="C-Type"
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Brand :", self.brand)
        print("Price :", self.price)
        print("ChargerType :", self.chargertype)
phone.chargertype="B-Type"
Samsung=phone("Samsung", 10000)
Samsung.display()
Redmi=phone("Redmi", 12000)
Redmi.display()
Google=phone("Google", 55000)
Google.display()