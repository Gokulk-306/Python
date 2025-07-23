class goa:
    name=""
    drink=""
    def party(self):
        print("Lets Party!")
    def beach(self):
        print("Lets go to Beach and Enjoy!")
ramesh=goa()
suresh=goa()
ramesh.name="Ramesh"
suresh.name="Suresh"
ramesh.drink="Yes"
suresh.drink="No"
print(ramesh.name)
print("Drink :",ramesh.drink)
ramesh.party()
print(suresh.name)
print("Drink :",suresh.drink)
suresh.beach()