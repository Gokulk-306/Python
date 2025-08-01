def int_to_words(num):
    if num == 0:
        return "Zero"  # Capitalized

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    result = ""

    if num >= 1000:
        result += ones[num // 1000] + " thousand "
        num %= 1000

    if num >= 100:
        result += ones[num // 100] + " hundred "
        num %= 100

    if num >= 20:
        result += tens[num // 10] + " "
        num %= 10

    elif num >= 10:
        result += teens[num-10] + " "
        num = 0

    if num < 10:
        result += ones[num] + " "
        num = 0

    return result.strip().title()  # Capitalize first letter of each word

a = int(input())
print(int_to_words(a))
