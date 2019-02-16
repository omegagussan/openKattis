import unittest
from computeOperations import computeOperations

class computeOperationsTest(unittest.TestCase):
  def testcase_oneChar(self):
    self.assertEqual(computeOperations("d"), 3)
  def testcase_abba(self):
    self.assertEqual(computeOperations("abba"), 8)
    
if __name__ == '__main__':
  unittest.main()