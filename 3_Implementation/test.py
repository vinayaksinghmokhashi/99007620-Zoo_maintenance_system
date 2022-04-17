from __future__ import print_function
from Class_Zoo import Zoo
from Class_staff import Staff
from Class_Customer import Customer
import pytest
obj= Customer()
obj2= Staff()
def test_addanimal():
    assert obj2.addanimal()(0) == "Tiger"
    assert obj2.addanimal()(1) == "Lion"

def test_animal_caretaker():
     assert obj.animal_caretaker(0) == "Tiger : Abraham A"
     assert obj.animal_caretaker(1) == "Lion : Amit B"