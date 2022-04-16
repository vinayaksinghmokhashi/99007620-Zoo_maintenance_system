class Zoo:
    """A dummy doctring."""
    def __init__(self, listofanimals):
        """A dummy doctring."""
        self.animal = ''
        self.animalspresent = listofanimals

    def displayanimals(self):
        """A dummy doctring."""
        # displays the animals present in zoo
        print("The animals:")
        print("================================")
        for animal in self.animalspresent:
            print(animal)

    def removeanimal(self):
        """A dummy doctring."""
        # Removes the animal from the zoo list
        print("Enter the name of animal you'd like to remove")
        self.animal = raw_input()
        if self.animal in self.animalspresent:
            print("The animal has been removed from the list")
            self.animalspresent.remove(self.animal)
        else:
            print("The entered animal is not found in the list")

    def addedanimal(self, addanimal):
        """A dummy doctring."""
        # Adds the animal from the zoo list
        try:
            addanimal = int(addanimal)
            print("Animal can't be number")
        except: # pylint: disable=bare-except
            self.animalspresent.append(addanimal)

    def checkanimal(self):
        """A dummy doctring."""
        # Checks whether the animal is present in the zoo or not
        print("Enter the name of animal you want to check for")
        self.animal = raw_input()
        if self.animal in self.animalspresent:
            print("The entered animal is present in the zoo")
        else:
            print("The entered animal is not found in the zoo")

    def __init__(self, listofanimals):
        """A dummy doctring."""
        self.details = None
        self.animalspresent = listofanimals

    def displayanimaldetails(self):
        """A dummy doctring."""
        # displays information of the animals present in zoo
        print("Details of the animal as follows:")
        print("================================")
        for animal in self.animalspresent:
            print(animal)


