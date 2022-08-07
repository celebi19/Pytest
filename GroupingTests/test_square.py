import pytest
import math

"""
     To group tests, use 'markers' <@pytest.mark.<markername> but first import
        pytest module in the test file
     To run the marked tests, use the following command <pytest -m <markername> -v>
     To run the tests marked as others, run the following command <pytest -m others -v> pytest -m others -vpytest -m others -v
 """

@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
   num = 7
   assert 7*7 == 40

@pytest.mark.others
def test_equality():
   assert 10 == 11