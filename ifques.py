a=int(input("Tamil Mark: "))
b=int(input("English Mark: "))
c=int(input("Maths Mark: "))
d=int(input("Science Mark: "))
e=int(input("Social Mark: "))
avg=(a+b+c+d+e)/5
if(avg <= 35):
    print ("Your Average score is: ",avg)
    print("Additional class is required for you")
else:
    print("Your Average score is: ", avg)
    print("You are good to go")
