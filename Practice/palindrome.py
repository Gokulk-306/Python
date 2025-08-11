str1 = input("Enter the string : ")
str = str1.lower()
str2 = ""

for i in range(len(str),0,-1):
    str2 += str[i-1]

if str2==str:
    print("The string is palindrome")
else:
    print("The string is not palindrome")