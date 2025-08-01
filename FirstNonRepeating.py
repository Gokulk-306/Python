def first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None
s=input("Enter the String :")
print(first_non_repeating_char(s))  # Output: w
