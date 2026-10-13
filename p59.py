#instance methods: rectangle area and perimeter
#problem: create a rectangle class with length and breath. use instance methods to calculate its area and perimeter.

class Rectangle:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath

    def perimeter(self):
        return 2 * (self.length + self.breath)