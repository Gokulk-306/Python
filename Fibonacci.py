def fibonacci(n):
    a=0
    b=1
    res=[]
    for i in range(n):
        res.append(str(a))
        a,b=b,a+b
    print(", ".join(res))
n=int(input("Enter the Number :"))
fibonacci(n)
