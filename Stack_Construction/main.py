from computeOperations import computeOperations
# import unittest

# class computeOperationsTest(unittest.TestCase):
#     def testcase_oneChar(self):
#         self.assertEqual(computeOperations("d"), 3)

#     def testcase_abba(self):
#         self.assertEqual(computeOperations("abba"), 8)

#     def testcase_harderRemoveOnlyTest(self):
#         self.assertEqual(computeOperations("rollover ahead"), 34)

#     def testcase_harderGoForward(self):
#         self.assertEqual(computeOperations("ogopogo spotted!"), 38)


# if __name__ == '__main__':
#     unittest.main()

import sys
rows = 0
for i in sys.stdin:
 if not rows == 0:
   print(computeOperations(str(i).strip()))
 else:
   rows = int(i)
