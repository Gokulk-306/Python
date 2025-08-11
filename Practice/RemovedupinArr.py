n = int(input("Enter the input : "))
arr=[]
arr2=[]
for i in range(n):
    num=int(input("Enter the input : "))
    arr.append(num)

arr2=list(set(arr))
print("The array after removing duplicate inputs :",arr2)