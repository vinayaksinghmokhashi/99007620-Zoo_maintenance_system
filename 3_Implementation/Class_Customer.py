class Customer:
    """A dummy doctring."""
    def __init__(self, listofanimals):
        """A dummy doctring."""
        self.location = listofanimals
        self.caretaker = listofanimals

    def animallocation(self):
        """A dummy doctring."""
        # Displayes the animal location
        print("The location of animals are as follows")
        print("=========================")
        for animal in self.location:
            print(animal)

    def animal_caretaker(self):
        """A dummy doctring."""
        print("Respective Animal' care takers are")
        print("=========================")
        for animal in self.caretaker:
            print(animal)
