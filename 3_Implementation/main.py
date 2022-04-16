from __future__ import print_function
import sys
from Class_Zoo import Zoo
from Class_staff import Staff
from Class_Customer import Customer

def main():
    """A dummy doctring."""
    zoo = Zoo(["Tiger", "Lion", "Deer", "Elephant", "Dog", "Monkey", "Zebra",
               "Wild Cat", "Bear", "Cheetah", "Leopard", "Fox","Panda", "Giraffe",
               "Western lowland gorillas", "Crocodiles"])
    details = Zoo(["Tiger: 1.Age:6 years  2.Class: Mammal  3.Gender: Male",
                   "Monkey: 1.Age:9 years  2.Class: Mammal  3.Gender: Female",
                   "Zebra: 1.Age:13 years  2.Class: Mammal  3.Gender: Male",
                   "Wild Cat: 1.Age:11 months  2.Class: Mammal  3.Gender: Female",
                   "Bear: 1.Age:21 years  2.Class: Mammal  3.Gender: Male",
                   "Cheetah: 1.Age:16 years  2.Class: Mammal  3.Gender: Male",
                   "Leopard: 1.Age:6 years  2.Class: Mammal  3.Gender: Female",
                   "Fox: 1.Age:5 years  2.Class: Mammal  3.Gender: Male",
                   "Lion: 1.Age:11 years  2.Class: Mammal  3.Gender: Female",
                   "Deer: 1.Age:5 years  2.Class: Mammal  3.Gender: Male",
                   "Elephant: 1.Age:18 years  2.Class: Mammal  3.Gender: Female",
                   "Dog: 1.Age:7 years  2.Class: Mammal  3.Gender: Male",
                   "Panda: 1.Age:6 months  2.Class: Mammal  3.Gender: Female",
                   "Giraffe: 1.Age:9 years  2.Class: Mammal  3.Gender: Female",
                   "Western lowland gorillas: 1.Age:29 years  2.Class: Mammal  3.Gender: Female",
                   "Crocodiles: 1.Age:6 years  2.Class: Reptile  3.Gender: Female",])
    animallocation = Customer(["Tiger : Block A", "Lion : Block D",
                               "Deer : Block F ", "Elephant : Block T",
                               "Dog : Block A", "Monkey : Block T",
                               "Zebra : Block Z", "Wild cat : Block W",
                               "Bear : Block B", "Cheetah : Block C",
                               "Leopard : Block L", "Fox : Block X",
                                "Lion : Block L", "Deer: Block D",
                               "Elephant: Block E", "Wild dog: Block D",
                               "Dog: Block D", "Panda:Block P",
                               "Giraffe: Block G", "Western lowland gorillas: Block D",
                               "Crocodiles: Block C"])
    animal_caretaker = Customer(["Tiger : Abraham A", "Lion : Amit B",
                                 "Deer : Subbu S ", "Elephant : Ashish A",
                                 "Wild Dog: Shubam M", "Panda: Omkar C", "Tiger: Chaitali B",
                                 "Giraffe: Kartik P", "Wedtern lowland Gorilla: Ashwin C",
                                 "Crocodile: Vandana D"
                                 ])
    staff = Staff()
    staff = Staff()
    #staff.addAnimal()
    done = False
    while not done:

        print(""" ======WELCOME TO ZOO=======
                  1. Display present animals
                  2. Add animal
                  3. Display detalils of animals  present
                  4. Remove animal
                  5. Check animal presence
                  6. View animal location
                  7. View animal caretaker
                  8. Exit
                  """)

        choice = int(input("Enter Choice:"))

        if choice == 1:
            zoo.displayanimals()
        elif choice == 2:
            zoo.addedanimal(staff.addanimal())
        elif choice == 4:
            zoo.removeanimal() 
        elif choice == 5:
            zoo.checkanimal()
        elif choice == 6:
            animallocation.animallocation()
        elif choice == 7:
            animal_caretaker.animal_caretaker()
        elif choice == 7:
            animal_caretaker.animal_caretaker()
        elif choice == 3:
            details.displayanimaldetails()
        elif choice == 8:
            print("""                            =====THANK YOU FOR VISITING=====
                    ===============DO VISIT AGAIN===============""")
            sys.exit()

main()