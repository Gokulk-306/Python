class laptop:
    Price=""
    Processor=""
    Ram=""
    def study(self):
        print("Suitable for study purpose")
    def gaming(self):
        print("Suitable for gaming purpose")
Hp=laptop()
Dell=laptop()
lenovo=laptop()
Hp.Price="45000"
Dell.Price="65000"
lenovo.Price="55000"
Hp.Processor="i3, 13th Gen"
Dell.Processor="i5, 13th Gen"
lenovo.Processor="Amd R5"
Hp.Ram="8gb"
Dell.Ram="8gb"
lenovo.Ram="8gb"
print("--- Hp laptop ---")
print ("Price :",Hp.Price)
print("Processor :",Hp.Processor)
print("Ram :",Hp.Ram)
Hp.study()
print("--- Dell laptop ---")
print ("Price :",Dell.Price)
print("Processor :",Dell.Processor)
print("Ram :",Dell.Ram)
Dell.study()
print("--- Lenovo laptop ---")
print ("Price :",lenovo.Price)
print("Processor :",lenovo.Processor)
print("Ram :",lenovo.Ram)
lenovo.gaming()





