class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Make the class iterable
    def __iter__(self):
        # Yield the length first
        yield {'length': self.length}
        # Yield the width second
        yield {'width': self.width}

# Example
rect = Rectangle(10, 5)

# Iterating over the Rectangle instance
for dimension in rect:
    print(dimension)
