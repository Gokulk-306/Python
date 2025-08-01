num = int(input("Enter a number: "))
arr=[]
for i in range(num):
    a=int(input("Enter the number "+(str(i+1))+" :"))
    arr.append(a)
def SecondLargest(arr):
    arr.sort()
    print(arr[-2])
result = SecondLargest(arr)