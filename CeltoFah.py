c=int(input("Enter the celsius temperature :"))
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(c),"F")