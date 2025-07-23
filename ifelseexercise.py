Salary=int(input("Salary Amount: "))
Age=int(input("Age: "))
if((Salary >= 20000) or (Age<=25)):
    loan =int(input("Loan:"))
    if(loan>50000):
        print("Your loan limit is 50000")
    else:
        print("Your loan will get approved")
else:
    print("You are not Eligible for applying loan")