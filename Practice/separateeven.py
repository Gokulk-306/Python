n=int(input("Enter the number : "))
arr=[]
arr2=[]
arr3=[]
for i in range(n):
    num=int(input("Enter the input : "))
    arr.append(num)
    if arr[i]%2==0:
        arr2.append(arr[i])
    else:
        arr3.append(arr[i])

print("The odd numbers from given array :",arr3)
print("The even numbers from given array :",arr2)

