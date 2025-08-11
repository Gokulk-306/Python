str=input("Enter the String : ")
str2=""
for i in range(len(str),0, -1):
    str2+=str[i-1]
print(str2)