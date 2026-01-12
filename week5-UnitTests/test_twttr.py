import pytest
from twttr import shorten

def test_lowercase_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("prompt") == "prmpt"
    assert shorten("faeiou") == "f"
def test_uppercase_shorten():
    assert shorten("twItter") == "twttr"