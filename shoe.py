class Shoe:
    def __init__(self, brand, size, color):
        """
        Constructor for the Shoe class.

        Parameters:
        - brand (str): The brand of the shoe.
        - size (int): The size of the shoe.
        - color (str): The color of the shoe.
        """
        self.brand = brand
        self.size = size
        self.color = color
        self.material = None  # Material attribute is initially set to None

    def set_material(self, material):
        """
        Sets the material of the shoe.

        Parameters:
        - material (str): The material to set for the shoe.
        """
        self.material = material

    def display_info(self):
        """
        Returns a string representation of the shoe's information.

        Returns:
        str: A string containing the shoe's color, brand, size, and material.
        """
        return f"{self.color} {self.brand} Shoes, Size {self.size}, Material: {self.material}"
