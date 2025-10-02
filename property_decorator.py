
class Circle:
    """
    A class representing a circle with properties for radius, area, circumference, and diameter.

    Attributes:
        radius (float): The radius of the circle. Must be non-negative.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle. Must be non-negative.
        """
        self._radius = radius

    @property
    def radius(self):
        """
        Get the radius of the circle.

        Returns:
            float: The current radius.
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        Set the radius of the circle.

        Args:
            value (float): The new radius value. Must be non-negative.

        Raises:
            ValueError: If the radius is negative.
        """
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14 * self._radius ** 2

    @property
    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * 3.14 * self._radius

    @property
    def diameter(self):
        """
        Calculate the diameter of the circle.

        Returns:
            float: The diameter of the circle.
        """
        return 2 * self._radius
    
c = Circle(5)
print(c.radius)  # Output: 5
print(c.area)    # Output: 78.5
print(c.circumference)  # Output: 31.400000000000002
print(c.diameter)  # Output: 10
c.radius = 10
print(c.radius)  # Output: 10
print(c.area)    # Output: 314.0    
print(c.circumference)  # Output: 62.800000000000004    
print(c.diameter)  # Output: 20    
# c.radius = -5  # Raises ValueError: Radius cannot be negative