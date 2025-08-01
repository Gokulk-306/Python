def Armstrong(num):
    count=0
    for i in num:
        if i.isdigit():
            count=count+1
    res = 0
    for i in num:
        if i.isdigit():
            res=res+(int(i)**count)
    return res
num = input("Enter a number: ")
res = Armstrong(num)
print("Result :",res)
if res == int(num):
    print("The number is Armstrong Number")
else:
    print("The number is not Armstrong Number")