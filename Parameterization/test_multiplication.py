import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output


   """ # Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using
         the following marker 
         <@pytest.mark.parametrize>
       # Pytest -k multiplication -v
   """