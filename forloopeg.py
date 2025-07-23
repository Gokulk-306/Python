n=[]
print("Enter the 10 numbers")
sum=0
count=0
avg=0
for i in range(10):
    num=int(input("Enter the number "+str(i+1)+" :"))
    n.append(num)
    sum=sum+i
    count=count+1
avg=sum/count
print("Sum of the value is :",sum)
print("Average of the value is :",avg)
