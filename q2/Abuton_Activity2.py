class Rectangle:
    def __init__(self, width, height):
        self.__width = width   
        self.__height = height 
    # --- GETTER METHODS ---
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # --- SETTER METHODS ---
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than zero")

    # --- DELETER METHODS ---
    @width.deleter
    def width(self):
        del self.__width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self.__height
        print("Height has been deleted")


# --- EXAMPLES / TESTING ---
rect = Rectangle(10, 5)

# Reading attributes 
print(f"Width: {rect.width}")
print(f"Height: {rect.height}")

# Modifying attributes 
rect.width = 15
rect.height = 20

print(f"Updated Width: {rect.width}")
print(f"Updated Height: {rect.height}")