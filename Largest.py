a=int(input("Enter the no of inputs :"))
n=[]
for i in range(a):
    num=int(input("Input "+str(i+1)+": "))
    n.append(num)
b=n[0]
for i in range(1,a):
    if n[i]>b:
        b=n[i]

print("The largest among the given number -->",b)