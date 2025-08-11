def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        fib=a+b
        a=b
        b=fib
n=int(input("Enter the number : "))
fibonacci(n)
