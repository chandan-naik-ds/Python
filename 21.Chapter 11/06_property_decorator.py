class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    
rectangle = Rectangle(3,4)

print(rectangle.width)
print(rectangle.height)

# print(rectangle._width)  # Should not write the private _width outside its class
# print(rectangle._height) # Should not write the private _height outside its class
