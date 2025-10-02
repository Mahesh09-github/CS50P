import pytest
from fuel2 import convert,guage

def test_convert():
    assert convert("3/4") == 0.75
    assert convert("1/4") == 0.25
    
def test_guage():
    assert guage(0.99) == "Full!!"
    assert guage(0.001) == "Empty!!"