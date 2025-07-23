str=input("Enter the string :")
str1=str.lower()
def count_vowels():
    count=0
    for char in str1:
        if char in 'aeiou':
            count=count+1
    print(count)
count_vowels()










