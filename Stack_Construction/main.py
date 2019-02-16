from computeOperations import computeOperations
import unittest

class computeOperationsTest(unittest.TestCase):
    def test_d(self):
        self.assertEqual(computeOperations("d"), 3)

    def test_abba(self):
        self.assertEqual(computeOperations("abba"), 8)

    def test_rollover_ahead(self):
        self.assertEqual(computeOperations("rollover ahead"), 34)

    def test_ogopogo_spotted(self):
        self.assertEqual(computeOperations("ogopogo spotted!"), 38)

    def test_willAddEvenIfInStack(self):
        self.assertEqual(computeOperations("bacacab"), 14)

if __name__ == '__main__':
    unittest.main()

# import sys
# rows = 0
# for i in sys.stdin:
#  if not rows == 0:
#    print(computeOperations(str(i).strip()))
#  else:
#    rows = int(i)
