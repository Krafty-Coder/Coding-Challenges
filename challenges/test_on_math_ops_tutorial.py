
import unittest
from ownmath import MathOperations # Not yet created the class and the module
# itself
class testMathematicalOperations(unittest.TestCase):  # We inherit from the
# unittest module
 “””
     This class is for testing on the mathematical operations
     These include; adding, subtracting and multiplication
 “””
 def setUp(self):
 “””
     This method/function creates an instance of the method i.e. the object we are
     testing but just for testing purposes
 “””
 self.operation = MathOperations()
 print(“setUp”) # This will show that our code actually runs the setup method
def tearDown(self):
 “””
     This method is actually used for clearing all the data after test is done
     This prevents having unnecessary data in the database which was created on
     running tests (For our case we won’t use it since we dont have an actual app
     on production)
 “””
 print(“tearDown”) # This shows that tear down is run after each and every test  
 #  has run
def test_on_addition(self):
 “””
     This method tests whith the add_numbers method(which we don’t have now) works
     fine and gives the desired output
 “””
 self.assertEqual(self.operation.add_numbers(2,4), 6)
 self.assertEqual(self.operation.add_numbers(3,5), 8)
 self.assertNotEqual(self.operation.add_numbers(2,5), 4)
def test_on_substraction(self):
 “””
     This method tests whether the subtract_numbers method(which we also don’t have now) works
     fine and gives the desired output
 “””
 self.assertEqual(self.operation.subtract_numbers(4,1), 3)
 self.assertEqual(self.operation.subtract_numbers(5,6), -1)
 self.assertEqual(self.operation.subtract_numbers(4,0), 4)
 self.assertEqual(self.operation.subtract_numbers(7,2), 5)
def test_on_multiply(self):
 “””
     This method tests whether the multiply_numbers method(which we obviously have now) works
     fine and gives the desired output :)
 “””
 self.assertEqual(self.operation.multiply_numbers(3,4), 12)
 self.assertEqual(self.operation.multiply_numbers(3,12), 36)
 self.assertEqual(self.operation.multiply_numbers(2,12), 24)
 self.assertEqual(self.operation.multiply_numbers(3,0), 0)
 self.assertNotEqual(self.operation.multiply_numbers(3,4), -12)
if __name__ == ‘__main__’:
 unittest.main()


