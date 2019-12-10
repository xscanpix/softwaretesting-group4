#!/usr/bin/env python27

import unittest
from collections import Counter
import itertools


class TestCounterBlackbox(unittest.TestCase):
    """
    * Blackbox test class for testing collections.Counter.
    * All tests are based on the documentation at https://docs.python.org/2/library/collections.html#collections.Counter

    It is an unordered collection where elements are stored as dictionary keys
    and their counts are stored as dictionary values.
    Counts are allowed to be any integer value including zero or negative counts.
    The Counter class is similar to bags or multisets in other languages.
    Elements are counted from an iterable or initialized from another mapping (or counter).
    """
    def test_counter_construct(self):
        self.skipTest("Not implemented!")

    def _count_counter_elements(self, counter):
        _n = 0

        for _ in counter.elements():
            _n = _n + 1

        return _n

    def test_counter_lengths(self):
        """
        Test len(Counter).
        """
        # Check empty Counter, no arguments
        c = Counter()
        self.assertEqual(len(c),   0)

        # Check empty Counter, empty 'set'
        c = Counter({})
        self.assertEqual(len(c), 0)

        # Check counter, empty 'list'
        c = Counter([])
        self.assertEqual(len(c), 0)

        # Check counter, empty 'iterable'
        c = Counter('')
        self.assertEqual(len(c), 0)

        # Check counter, filled 'set'
        c = Counter({'a', 'b', 'c'})
        self.assertEqual(len(c), 3)

        # Check counter, filled 'set' and duplicates
        c = Counter({'a', 'b', 'c', 'a'})
        self.assertEqual(len(c), 3)

        # Check counter, filled 'list'
        c = Counter(['a', 'b', 'c'])
        self.assertEqual(len(c), 3)

        # Check counter, filled 'list' and duplicates
        c = Counter(['a', 'b', 'c', 'a'])
        self.assertEqual(len(c), 3)

        # Check counter, filled 'iterable'
        c = Counter('abc')
        self.assertEqual(len(c), 3)

        # Check counter, filled 'iterable' and duplicates
        c = Counter('abc')
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'dict' (zeros)
        c = Counter({'a': 0, 'b': 0, 'c': 0})
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'dict' (positive)
        c = Counter({'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'dict' (negative)
        c = Counter({'a': -1, 'b': -1, 'c': -1})
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'dict', duplicates
        c = Counter({'a': 1, 'b': 1, 'c': 1, 'a': 1})
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'keyword args'
        c = Counter(a=2, b=2, c=2)
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'keyword args' (zeroes)
        c = Counter(a=0, b=0, c=0)
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'keyword args' (negative)
        c = Counter(a=-1, b=-1, c=-1)
        self.assertEqual(len(c), 3)

        # Check counter with argument type 'keyword args' (mixed)
        c = Counter(a=-1, b=0, c=2)
        self.assertEqual(len(c), 3)

    def test_counter_f_elements(self):
        """
        Test Counter.elements().
        Return an iterator chain over elements repeating each as many times as its count.
        Elements are returned in arbitrary order.
        If an element's count is less than one, elements() will ignore it.
        """
        # Check empty Counter, no arguments
        c = Counter()
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check empty Counter, empty 'set'
        c = Counter({})
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check counter, empty 'list'
        c = Counter([])
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check counter, empty 'iterable'
        c = Counter('')
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check counter, filled 'set'
        c = Counter({'a', 'b', 'c'})
        self.assertEqual(self._count_counter_elements(c), 3)

        # Check counter, filled 'set' and duplicates ('set' cannot contain duplicates)
        c = Counter({'a', 'b', 'c', 'a'})
        self.assertEqual(self._count_counter_elements(c), 3)

        # Check counter, filled 'list'
        c = Counter(['a', 'b', 'c'])
        self.assertEqual(self._count_counter_elements(c), 3)

        # Check counter, filled 'list' and duplicates
        c = Counter(['a', 'b', 'c', 'a'])
        self.assertEqual(self._count_counter_elements(c), 4)

        # Check counter, filled 'iterable'
        c = Counter('abc')
        self.assertEqual(self._count_counter_elements(c), 3)

        # Check counter, filled 'iterable' and duplicates
        c = Counter('abca')
        self.assertEqual(self._count_counter_elements(c), 4)

        # Check counter with argument type 'dict' (zeros)  (zeroes are ignored)
        c = Counter({'a': 0, 'b': 0, 'c': 0})
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check counter with argument type 'dict' (positive)
        c = Counter({'a': 2, 'b': 2, 'c': 2})
        self.assertEqual(self._count_counter_elements(c), 6)

        # Check counter with argument type 'dict' (negative) (negatives are ignored)
        c = Counter({'a': -1, 'b': -1, 'c': -1})
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check counter with argument type 'dict' (mixed)
        c = Counter({'a': -1, 'b': 0, 'c': 2})
        self.assertEqual(self._count_counter_elements(c), 2)

        # Check counter with argument type 'dict', duplicates
        c = Counter({'a': 2, 'b': 2, 'c': 2, 'a': 1})
        self.assertEqual(self._count_counter_elements(c), 5)

        # Check counter with argument type 'keyword args'
        c = Counter(a=2, b=2, c=2)
        self.assertEqual(self._count_counter_elements(c), 6)

        # Check counter with argument type 'keyword args' (zeroes)
        c = Counter(a=0, b=0, c=0)
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check counter with argument type 'keyword args' (negative)
        c = Counter(a=-1, b=-1, c=-1)
        self.assertEqual(self._count_counter_elements(c), 0)

        # Check counter with argument type 'keyword args' (mixed)
        c = Counter(a=-1, b=0, c=2)
        self.assertEqual(self._count_counter_elements(c), 2)

    def test_counter_f_most_common(self):
        """
        Test Counter.most_common()
        Return a list of the n most common elements and their counts from the most common to the least.
        If n is omitted or None, most_common() returns all elements in the counter.
        Elements with equal counts are ordered arbitrarily.
        """
        self.skipTest("Not implemented!")

    def test_counter_f_subtract(self):
        """
        Test Counter.subtract()
        Elements are subtracted from an iterable or from another mapping (or counter).
        Like dict.update() but subtracts counts instead of replacing them.
        Both inputs and outputs may be zero or negative.
        """
        self.skipTest("Not implemented!")

    def test_counter_f_from_keys(self):
        """
        Counter.from_keys() is not implemented for Counter.
        Should raise an NotImplementedError exception.
        """
        c = Counter()
        it = (1, 2, 3)

        with self.assertRaises(NotImplementedError):
            c.fromkeys(it)

    def test_counter_f_update(self):
        """
        Test Counter.update()
        Elements are counted from an iterable or added-in from another mapping (or counter).
        Like dict.update() but adds counts instead of replacing them.
        Also, the iterable is expected to be a sequence of elements, not a sequence of (key, value) pairs.
        """
        self.skipTest("Not implemented!")

    def test_counter_count_missing(self):
        """
        Counter objects have a dictionary interface except that they return a
        zero count for missing items instead of raising a KeyError:
        """
        self.skipTest("Not implemented!")

    def test_counter_set_zero_and_delete(self):
        """
        Test setting an element to zero and deleting the element.
        Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:
        """
        pass

    def test_counter_to_set(self):
        self.skipTest("Not implemented!")

    def test_counter_to_list(self):
        self.skipTest("Not implemented!")

    def test_counter_to_dict(self):
        self.skipTest("Not implemented!")

    def test_counter_items(self):
        self.skipTest("Not implemented!")

    def test_counter_remove_zero_negative(self):
        self.skipTest("Not implemented!")

    def test_counter_addition_other(self):
        """
        Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements.
        """
        self.skipTest("Not implemented!")

    def test_counter_subtract_other(self):
        """
        Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements.
        """
        self.skipTest("Not implemented!")

    def test_counter_intersection_other(self):
        self.skipTest("Not implemented!")

    def test_counter_union_other(self):
        self.skipTest("Not implemented!")


if __name__ == '__main__':
    unittest.main()
