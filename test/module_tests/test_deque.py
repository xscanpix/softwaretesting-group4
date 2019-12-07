#!/usr/bin/env python3

import collections
import unittest


class TestDeque(unittest.TestCase):

  """ test_iteratable_construct
  Black box testing the deque constructor of no paramters and an iteratable constructor
  The test case verifies that no paramters returns an empty collection whilst an iteratable parameters returns a none-empty collection

  Purpose: Verify that the constructors are working according to the documentation (giving non empty list will fill up the deque collection)
  """
  def test_iteratable_construct(self):
    emptyDeque = collections.deque()
    noneEmptyDeque = collections.deque(["Hello", 123, "world", "456"])
    self.assertEqual(len(emptyDeque), 0)
    self.assertTrue(len(noneEmptyDeque) > 0)

  """ test_append_pop_right
  Black box testing the deque append and pop right functions (pop end of collection).
  The collection follows a queue datastructure with two ends.
  Poping from the right is considered default queue behavior and should return in order according to FILO (first in, last out).
  
  Purpose: Verify that the order of the values being appended to the queue and poped in the reversed order according to FILO
  """
  def test_append_pop_right(self):
    deque = collections.deque()
    deque.append("asd")
    deque.append("ow")
    deque.append(75)
    self.assertTrue(len(deque) > 0)
    self.assertEqual(deque.pop(), 75)
    self.assertEqual(deque.pop(), "ow")
    self.assertEqual(deque.pop(), "asd")
    self.assertEqual(len(deque), 0)

  """ test_append_pop_left
  Black box testing the deque append and pop left functions (pop start of collection).

  Purpose: Verify that the same behavior as in pop right is observed if direction is reversed
  """
  def test_append_pop_left(self):
    deque = collections.deque()
    deque.appendleft("left")
    deque.appendleft("captain")
    deque.appendleft("card")
    self.assertTrue(len(deque) > 0)
    self.assertEqual(deque.popleft(), "card")
    self.assertEqual(deque.popleft(), "captain")
    self.assertEqual(deque.popleft(), "left")
    self.assertEqual(len(deque), 0)

  """ test_append_right_pop_left
  Black box testing the deque append right and pop left
  The behavior we should observe is, contrary to two previous tests, a FIFO (first in, first out)

  Purpose: Verify that the order of the values being appended are pop'd in a queue like manner rather than a stack behavior
  """
  def test_append_right_pop_left(self):
    deque = collections.deque()
    deque.append("tree")
    deque.append("bark")
    deque.append(133)
    self.assertTrue(len(deque) > 0)
    self.assertEqual(deque.popleft(), "tree")
    self.assertEqual(deque.popleft(), "bark")
    self.assertEqual(deque.popleft(), 133)
    self.assertEqual(len(deque), 0)

  """ test_append_right_pop_left
  Black box testing the deque append left and pop right

  Purpose: Verify that the behavior is the same as in test_append_right_pop_left using reserved order
  """
  def test_append_left_pop_right(self):
    deque = collections.deque()
    deque.appendleft("tree")
    deque.appendleft("bark")
    deque.appendleft(133)
    self.assertTrue(len(deque) > 0)
    self.assertEqual(deque.pop(), "tree")
    self.assertEqual(deque.pop(), "bark")
    self.assertEqual(deque.pop(), 133)
    self.assertEqual(len(deque), 0)

  """ test_clear
  Black box testing clearing of a collection (deque)

  Purpose: assert that lists are properly cleared
  """
  def test_clear(self):
    deque = collections.deque(["Boat", "cruiser", "train"])
    self.assertTrue(len(deque) > 0)
    deque.clear()
    self.assertTrue(len(deque) == 0)

  """ test_count
  Black box for deque count elements in the list

  Purpose: verify that elements are properly counted
  """
  def test_count(self):
    deque = collections.deque([10, 10, 10, 10, 2, 3, 10, 10, 1, 10, 1000, 10, 10])
    self.assertEqual(deque.count(0), 0)
    self.assertEqual(deque.count(10), 9)
    self.assertEqual(deque.count(2), 1)
    self.assertEqual(deque.count(3), 1)

  """ test_extend_right
  Black box testing for extension of list from the right

  Purpose: verify that elements are properly extended in a queue like fashion
  """
  def test_extend_right(self):
    deque = collections.deque(["hello", "world"])
    self.assertTrue(len(deque) == 2)
    deque.extend(["World", "Hello"])
    self.assertTrue(len(deque) == 4)
    self.assertEqual(deque.pop(), "Hello")
    self.assertEqual(deque.pop(), "World")
    self.assertEqual(deque.pop(), "world")
    self.assertEqual(deque.pop(), "hello")
    self.assertTrue(len(deque) == 0)

  """ test_extend_left
  Black box testing for extension of list from left
  NOTE: Values extended SHOULD be extended in a reversed like fashion according to the docs

  Purpose: verify that elements are properly extended in a reverse like fashion
  """
  def test_extend_left(self):
    deque = collections.deque(["hello", "world"])
    self.assertTrue(len(deque) == 2)
    deque.extendleft(["World", "Hello"])
    self.assertTrue(len(deque) == 4)
    self.assertEqual(deque.pop(), "world")
    self.assertEqual(deque.pop(), "hello")
    self.assertEqual(deque.pop(), "World")
    self.assertEqual(deque.pop(), "Hello")
    self.assertTrue(len(deque) == 0)

  """ test_deque_remove_first
  Black box testing for removal of first occurance (not all)

  Purpose: verify that only the first occurance is removed from the collection
  """
  def test_deque_remove_first(self):
    deque = collections.deque(["hello", "world", "world", "hello"])
    self.assertTrue(len(deque) == 4)
    self.assertEqual(deque.count("world"), 2)
    deque.remove("world")
    self.assertTrue(len(deque) == 3)
    self.assertEqual(deque.count("world"), 1)
    deque.remove("world")
    self.assertTrue(len(deque) == 2)
    self.assertEqual(deque.count("world"), 0)
    

  """ test_reverse
  Black box testing for reversal of a deque collection

  Purpose: verify that reversing a list turns it from a stack like fashion to a queue like fashion
  """
  def test_reverse(self):
    deque = collections.deque(["hello", "world", "World", "Hello"])
    self.assertTrue(len(deque) == 4)
    deque.reverse()
    self.assertTrue(len(deque) == 4)
    self.assertEqual(deque.pop(), "hello")
    self.assertEqual(deque.pop(), "world")
    self.assertEqual(deque.pop(), "World")
    self.assertEqual(deque.pop(), "Hello")
    
  """ test_rotate
  Black box testing for rotation of a deque collection
  NOTE: no provided parameters should default to rotation for one step

  Purpose: verify that no paramters rotates 1 step and that it works after removing elements
  """
  def test_rotate(self):
    deque = collections.deque(["hello", "world", "World", "Hello"])
    self.assertTrue(len(deque) == 4)
    deque.rotate() #default one step ["Hello", "hello", "world", "World"]
    self.assertEqual(deque.pop(), "World")
    deque.rotate(2) #["world", "hello", "Hello"]
    self.assertEqual(deque.pop(), "Hello")

  """ test_maxlen_propert
  Black box testing that max len is working according to documentations
  NOTE: max len should be none if no max len is set in the constructor

  Purpose: verify that maxlen has the value of none if not set or set value if passed to constructor
  """
  def test_maxlen_property(self):
    deque = collections.deque(["hello", "world", "World", "Hello"])
    self.assertIsNone(deque.maxlen)
    deque = collections.deque(["hello", "world", "World", "Hello"], maxlen = 10)
    self.assertEqual(deque.maxlen, 10)
    
  """ test_maxlen_cut
  Black box testing that max length is enforced through the constructor

  Purpose: verify that if a max len value lower than the length of the iterable list passed to the constructor is set then it cuts the list to the maxlen value
  """
  def test_maxlen_cut(self):
    deque = collections.deque(["hello", "world", "World", "Hello"], maxlen=2)
    self.assertEqual(len(deque), 2)
    
    
if __name__ == '__main__':
  unittest.main()

