n=int(input("Enter the number:"))
a=[]
for i in range(n):
    b=int(input("Enter the input "+str(i+1)+" :"))
    a.append(b)
def Sum0fEven():
    sum=0
    for i in range(n):
        if(a[i]%2==0):
            sum=sum+a[i]
    return sum
print(Sum0fEven())
