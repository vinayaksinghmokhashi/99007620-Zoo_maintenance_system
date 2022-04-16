class Staff:
    """A dummy doctring."""

    def __init__(self):
        """A dummy doctring."""
        self.animal = None

    def addanimal(self):
        """A dummy doctring."""
        print("Enter the name of the animal you'd like to add>>")
        self.animal = raw_input()
        return self.animal
