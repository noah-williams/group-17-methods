import pytest
from functions import *

@pytest.mark.parametrize("file",["testing.txt", "ThisFileDoesNotExist.txt"])
def test_openFile(file):
    assert openFile(file) == None

@pytest.mark.parametrize("value1,value2,sum", [(3, 0, 0), ("6", "2", 3), (6, 3, 2), (10.4, 5.2, 2), (15, 7.5, 2), (-4, -2, 2)])
def test_numbers(value1, value2, sum):
    assert numbers(value1, value2) == sum

@pytest.mark.parametrize("x1,y1,x2,y2,sum", [(1, 1, 4, 5, 5), ("1", "1", "4", "5", 5), (1.1, 1.1, 4.1, 5.1, 5), (-1, -1, -4, -5, 5)])
def test_dist(x1, y1, x2, y2, sum):
    assert dist(x1, y1, x2, y2) == sum