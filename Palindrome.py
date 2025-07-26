String=input("Enter the string :")
str2=String.lower()
Rev_String=""
for char in str2:
    Rev_String=Rev_String+char
if str2==Rev_String:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

