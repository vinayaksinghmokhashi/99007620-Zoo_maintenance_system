from __future__ import print_function
from Class_Zoo import Zoo
from Class_staff import Staff
from Class_Customer import Customer
import pytest
obj= Zoo(0)
obj2= Staff(0)
def test_addanimal_fun():
    assert obj2.addanimal_fun()(0) == "Tiger"
    assert obj2.addanimal_fun()(1) == "Lion"
    assert obj2.addanimal_fun()(0) == "Tiger"
    assert obj2.addanimal_fun()(0) == "Deer"

def test_animal_caretaker_fun():
     assert obj.animal_caretaker_fun(0) == "Tiger : Abraham A"
     assert obj.animal_caretaker_fun(1) == "Lion : Amit B"
     assert obj.animal_caretaker_fun(2) == "Deer : Subbu S"
     assert obj.animal_caretaker_fun(3) == "Elephant : Ashish A"
