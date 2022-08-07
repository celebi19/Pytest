

import pytest

"""
     To group tests, use 'markers' <@pytest.mark.<markername> but first import
        pytest module in the test file
     To run the marked tests, use the following command <pytest -m <markername> -v>
"""

@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200



