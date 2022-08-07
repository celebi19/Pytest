import pytest
import math

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

def test_square_failure():
   num = 7
   assert 7*7 == 40

def test_equality_failure():
   assert 10 == 11


   """ # To stop the execution of test suite soon after n number of test fails. This can be done in pytest 
   using maxfail.
   # Use < pytest --maxfail = <num>> to stop test after n number of test run
   # pytest test_failure.py -v --maxfail=1 - test will stop if 1 test fails out of the 3 tests here
   """