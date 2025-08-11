num = int(input("Enter a number: "))

if num < 2:
    print("No, the number is not prime")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Only check up to √num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Yes, the number is prime")
    else:
        print("No, the number is not prime")
