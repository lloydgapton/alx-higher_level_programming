import math


class MagicClass:
    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with an optional radius.

        Parameters:
        - radius: The radius of the circle (private instance attribute).
                  Default value is 0.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.

        Returns:
        - The area of the circle (pi * radius^2).
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Computes and returns the circumference of the circle.

        Returns:
        - The circumference of the circle (2 * pi * radius).
        """
        return 2 * math.pi * self.__radius
