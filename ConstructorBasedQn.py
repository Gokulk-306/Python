class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        print("Area:", self.area())  # Call method here

    def area(self):
        return self.width * self.length

# Object creation
ob = Rectangle(10, 10)
