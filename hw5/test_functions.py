import pytest
from functions import *

@pytest.mark.parametrize("file",["testing.txt", "testing"])
def test_openFile(file):
    assert openFile(file) == None

@pytest.mark.parametrize("value1,value2,sum", [(3, 0, 0), ("6", "2", 3), (-6, 2, 3)])
def test_numbers(value1, value2, sum):
    assert numbers(value1, value2) == sum