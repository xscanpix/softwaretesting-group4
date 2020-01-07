#!/usr/bin/env python27

import unittest
from collections import Counter


def _count_counter_elements(counter):
    """ private method for counting elements """
    _n = 0

    for _ in counter.elements():
        _n = _n + 1

    return _n


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
    def test_counter01_construct(self):
        """
        Test constructing a counter with different input argument types.

        Each valid construction boils down to a dict().
        Test each different argument type here, later only dict() have to be tested.

        Purpose:
            Check if constructing throws an TypeError on construction.

            Check if construction with valid arguments are equal.
        """
        with self.assertRaises(TypeError):
            Counter(1) # Integer is not iterable

        with self.assertRaises(TypeError):
            Counter(2.2) # Float is not iterable

        try:
            Counter()  # Emtpy
            Counter(dict())  # Empty dict
            Counter('')  # Empty iterable
            Counter({})  # Empty set
            Counter('123')  # Non-empty iterable
            Counter({'1': 1, '2': 2})  # Non-empty dict
            Counter(a=1, b=2)  # keyword-args
        except TypeError:
            self.fail("Counter construction failed with supposedly valid input argument.")

        # Test equality
        c = Counter('')
        c0 = Counter('1')
        self.assertNotEqual(c, c0)

        c1 = Counter()
        c2 = Counter('')
        c3 = Counter({})

        self.assertEqual(c1, c2)
        self.assertEqual(c1, c3)
        self.assertEqual(c2, c3)

        c4 = Counter('aabc')
        c5 = Counter({'a': 2, 'b': 1, 'c': 1})
        c6 = Counter(a=2, b=1, c=1)

        self.assertEqual(c4, c5)
        self.assertEqual(c4, c6)
        self.assertEqual(c5, c6)

    def test_counter02_lengths(self):
        """
        Test len(Counter).

        Purpose:
            Check if Counters constructed with different arguments have the correct length.
            Only dict() necessary to test.
        """
        # Check empty Counter, no arguments
        c = Counter()
        self.assertEqual(len(c),   0)

        # Check counter, filled 'set'
        c = Counter({'a': 1, 'b': 1, 'c': 1})
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

        # Check counter with argument type 'keyword args' (mixed)
        c = Counter({'a': -1, 'b': 0, 'c': 2})
        self.assertEqual(len(c), 3)

    def test_counter03_f_elements(self):
        """
        Test Counter.elements().
        Return an iterator chain over elements repeating each as many times as its count.
        Elements are returned in arbitrary order.
        If an element's count is less than one, elements() will ignore it.
        """
        # Check empty Counter, no arguments
        c = Counter()
        self.assertEqual(_count_counter_elements(c), 0)

        # Check empty Counter, empty 'dict'
        c = Counter(dict())
        self.assertEqual(_count_counter_elements(c), 0)

        # Check counter, filled 'dict'
        c = Counter({'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(_count_counter_elements(c), 3)

        # Check counter, filled 'set' and duplicates ('dict' cannot contain duplicates)
        c = Counter({'a': 1, 'b': 1, 'c': 1, 'a': 1})
        self.assertEqual(_count_counter_elements(c), 3)

        # Check counter with argument type 'dict' (zeros)  (zeroes are ignored)
        c = Counter({'a': 0, 'b': 0, 'c': 0})
        self.assertEqual(_count_counter_elements(c), 0)

        # Check counter with argument type 'dict' (positive)
        c = Counter({'a': 2, 'b': 2, 'c': 2})
        self.assertEqual(_count_counter_elements(c), 6)

        # Check counter with argument type 'dict' (negative) (negatives are ignored)
        c = Counter({'a': -1, 'b': -1, 'c': -1})
        self.assertEqual(_count_counter_elements(c), 0)

        # Check counter with argument type 'dict' (mixed)
        c = Counter({'a': -1, 'b': 0, 'c': 2})
        self.assertEqual(_count_counter_elements(c), 2)

    def test_counter04_f_most_common(self):
        """
        Test Counter.most_common()
        Return a list of the n most common elements and their counts from the most common to the least.
        If n is omitted or None, most_common() returns all elements in the counter.
        Elements with equal counts are ordered arbitrarily.

        Purpose:
            Test whether the method returns the correct most common elements.
        """
        sorted_least_most = Counter({'1': 1, '2': 2, '3': 3, '4': 4})
        sorted_most_least = Counter({'1': 4, '2': 3, '3': 2, '4': 1})
        sorted_with_equals = Counter({'1': 4, '2': 3, '3': 3, '4': 2})
        random = Counter({'1': 3, '2': 1, '3': 2, '4': 5})

        # Test select all
        self.assertEqual(sorted_least_most.most_common(), [('4', 4), ('3', 3), ('2', 2), ('1', 1)])
        self.assertEqual(sorted_most_least.most_common(), [('1', 4), ('2', 3), ('3', 2), ('4', 1)])
        #self.assertIn(sorted_with_equals.most_common(), [[('1', 4), ('2', 3), ('3', 3), ('4', 1)], [('1', 4), ('3', 3), ('2', 3), ('4', 1)]])
        self.assertEqual(random.most_common(), [('4', 5), ('1', 3), ('3', 2), ('2', 1)])

    def test_counter05_f_subtract(self):
        """
        Test Counter.subtract()
        Elements are subtracted from an iterable or from another mapping (or counter).
        Like dict.update() but subtracts counts instead of replacing them.
        Both inputs and outputs may be zero or negative.
        """

        self.skipTest("Not implemented!")

    def test_counter06_f_from_keys(self):
        """
        Counter.from_keys() is not implemented for Counter.
        Should raise an NotImplementedError exception.
        """
        c = Counter()
        it = (1, 2, 3)

        with self.assertRaises(NotImplementedError):
            c.fromkeys(it)

    def test_counter07_f_update(self):
        """
        Test Counter.update()
        Elements are counted from an iterable or added-in from another mapping (or counter).
        Like dict.update() but adds counts instead of replacing them.
        Also, the iterable is expected to be a sequence of elements, not a sequence of (key, value) pairs.
        """
        self.skipTest("Not implemented!")

    def test_counter08_count_missing(self):
        """
        Counter objects have a dictionary interface except that they return a
        zero count for missing items instead of raising a KeyError:
        """
        self.skipTest("Not implemented!")

    def test_counter09_set_zero_and_delete(self):
        """
        Test setting an element to zero and deleting the element.
        Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:
        """
        self.skipTest("Not implemented!")

    def test_counter10_to_set(self):
        self.skipTest("Not implemented!")

    def test_counter11_to_list(self):
        self.skipTest("Not implemented!")

    def test_counter12_to_dict(self):
        self.skipTest("Not implemented!")

    def test_counter13_items(self):
        self.skipTest("Not implemented!")

    def test_counter14_remove_zero_negative(self):
        self.skipTest("Not implemented!")

    def test_counter15_addition_other(self):
        """
        Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements.
        """
        self.skipTest("Not implemented!")

    def test_counter16_subtract_other(self):
        """
        Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements.
        """
        self.skipTest("Not implemented!")

    def test_counter17_intersection_other(self):
        self.skipTest("Not implemented!")

    def test_counter18_union_other(self):
        self.skipTest("Not implemented!")


if __name__ == '__main__':
    unittest.main()
