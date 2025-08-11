s = input("Enter the string : ")
vowels = set("aeiouAEIOU")
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)
