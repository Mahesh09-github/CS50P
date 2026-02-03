import pytest
from um import count
def test_count():
    assert count("hello, um, world") == 1
    assert count("um?") == 1
    assert count("um.,Thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yummy") == 0