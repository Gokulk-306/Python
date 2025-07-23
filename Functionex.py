a=int(input("Enter a number: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
if(is_prime(a) == False):
    print("Not a prime number")
else:
    print("Prime number")
