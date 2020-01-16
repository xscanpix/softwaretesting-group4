

import unittest
import sys

PATH = "" + "/test/module_tests"
sys.path.append(PATH)

import collections_python


 """ test_pop_whitebox
  Whitebox testing of deque pop function

  Purpose: 100% test coverage meaning we test all of the code within the method
  we want to test all the paths possible going through the method
  See project report for description of paths
  """


class TestWhitebox(unittest.TestCase):

    def test_pop_whitebox(self):
        #path [1, 2]
        deque = collections_python.deque()
        n = 15
        with self.assertRaises(IndexError):
            deque.pop()

        #path [1, 3, 4, 5, 7]
        for i in range(n):
                deque.appendleft(n-i)
        
        self.assertEqual(len(deque), n)
        #deque.append(n+1)

        #path [1, 3, 7] gets visited here
        for i in range(n):
                self.assertEqual(deque.pop(), n-i)

        deque.appendleft(0)
        self.assertEqual(deque.pop(), 0)

        #path [1, 3, 4, 6, 7]
        deque.clear()

        for i in range(n):
                deque.append(i)
        self.assertEqual(len(deque), n)

        self.assertEqual(deque.pop(), n-1)

        #path [1, 3, 7] tested already



if __name__ == '__main__':
    unittest.main()
